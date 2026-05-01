import psycopg2
import json
import csv
from connect import connect

def filter_by_group(conn):
    group_name = input("Enter group name to filter by: ")
    with conn.cursor() as cur:
        cur.execute("""
            SELECT c.name, c.email, c.birthday 
            FROM contacts c
            JOIN groups g ON c.group_id = g.id
            WHERE g.name ILIKE %s
        """, (group_name,))
        results = cur.fetchall()
        print("\n--- Results ---")
        if not results:
            print("No contacts found in this group.")
        for row in results:
            print(f"Name: {row[0]}, Email: {row[1]}, Birthday: {row[2]}")

def search_by_email(conn):
    email_query = input("Enter partial email to search (e.g. gmail): ")
    with conn.cursor() as cur:
        cur.execute("SELECT name, email FROM contacts WHERE email ILIKE %s", (f'%{email_query}%',))
        results = cur.fetchall()
        print("\n--- Results ---")
        if not results:
            print("No contacts found.")
        for row in results:
            print(f"Name: {row[0]}, Email: {row[1]}")

def paginated_view(conn):
    sort_options = {'1': 'name', '2': 'birthday', '3': 'date_added'}
    print("\nSort by: 1. Name  2. Birthday  3. Date Added")
    choice = input("Choice (default 1): ")
    sort_col = sort_options.get(choice, 'name')
    
    limit = 5
    offset = 0
    while True:
        with conn.cursor() as cur:
            cur.execute(f"SELECT name, email, birthday FROM contacts ORDER BY {sort_col} LIMIT %s OFFSET %s", (limit, offset))
            results = cur.fetchall()
            
            print(f"\n--- Page {offset//limit + 1} ---")
            if not results:
                print("No more records.")
            else:
                for row in results:
                    print(f"Name: {row[0]}, Email: {row[1]}, Birthday: {row[2]}")
                    
        cmd = input("\n[n] Next page  [p] Prev page  [q] Quit: ").lower()
        if cmd == 'n':
            if len(results) == limit: # Only go next if current page is full
                offset += limit
        elif cmd == 'p':
            if offset >= limit:
                offset -= limit
        elif cmd == 'q':
            break

def export_to_json(conn):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT c.name, c.email, TO_CHAR(c.birthday, 'YYYY-MM-DD') as birthday, g.name as group,
                   COALESCE(json_agg(json_build_object('phone', p.phone, 'type', p.type)) FILTER (WHERE p.id IS NOT NULL), '[]') as phones
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
            LEFT JOIN phones p ON c.id = p.contact_id
            GROUP BY c.id, g.name
        """)
        columns = [desc[0] for desc in cur.description]
        data = [dict(zip(columns, row)) for row in cur.fetchall()]
        
    with open('contacts_export.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print("\nExported to contacts_export.json successfully.")

def import_from_json(conn):
    filepath = input("Enter JSON file path (e.g. contacts.json): ")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        with conn.cursor() as cur:
            for item in data:
                # Check for duplicate
                cur.execute("SELECT id FROM contacts WHERE name = %s", (item['name'],))
                existing = cur.fetchone()
                
                if existing:
                    action = input(f"Contact '{item['name']}' already exists. [s]kip or [o]verwrite? ").lower()
                    if action == 's':
                        continue
                    elif action == 'o':
                        cur.execute("DELETE FROM contacts WHERE id = %s", (existing[0],))
                        # Cascading delete handles phones automatically
                
                # Insert Group if provided
                group_id = None
                if item.get('group'):
                    cur.execute("SELECT id FROM groups WHERE name = %s", (item['group'],))
                    res = cur.fetchone()
                    if res:
                        group_id = res[0]
                    else:
                        cur.execute("INSERT INTO groups (name) VALUES (%s) RETURNING id", (item['group'],))
                        group_id = cur.fetchone()[0]

                # Insert Contact
                cur.execute("""
                    INSERT INTO contacts (name, email, birthday, group_id) 
                    VALUES (%s, %s, %s, %s) RETURNING id
                """, (item['name'], item.get('email'), item.get('birthday'), group_id))
                contact_id = cur.fetchone()[0]
                
                # Insert Phones
                for p in item.get('phones', []):
                    cur.execute("INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                                (contact_id, p['phone'], p['type']))
            conn.commit()
            print("\nJSON Import completed.")
    except FileNotFoundError:
        print("\nError: File not found.")
    except Exception as e:
        print(f"\nError importing JSON: {e}")
        conn.rollback()

def import_from_csv(conn):
    filepath = input("Enter CSV file path (e.g. contacts.csv): ")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            with conn.cursor() as cur:
                for row in reader:
                    name = row.get('name')
                    email = row.get('email')
                    # Handle empty birthday string
                    birthday = row.get('birthday')
                    if not birthday: birthday = None
                    
                    group_name = row.get('group_name')
                    phone = row.get('phone')
                    phone_type = row.get('phone_type', 'mobile')

                    if not name:
                        continue

                    # Check if contact exists
                    cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
                    existing = cur.fetchone()
                    
                    if existing:
                        contact_id = existing[0]
                    else:
                        # Handle Group
                        group_id = None
                        if group_name:
                            cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
                            res = cur.fetchone()
                            if res:
                                group_id = res[0]
                            else:
                                cur.execute("INSERT INTO groups (name) VALUES (%s) RETURNING id", (group_name,))
                                group_id = cur.fetchone()[0]

                        # Insert new contact
                        cur.execute("""
                            INSERT INTO contacts (name, email, birthday, group_id) 
                            VALUES (%s, %s, %s, %s) RETURNING id
                        """, (name, email, birthday, group_id))
                        contact_id = cur.fetchone()[0]
                    
                    # Add phone if provided
                    if phone:
                        cur.execute("INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                                    (contact_id, phone, phone_type))
                
                conn.commit()
                print("\nCSV Import completed.")
    except FileNotFoundError:
        print("\nError: File not found.")
    except Exception as e:
        print(f"\nError importing CSV: {e}")
        conn.rollback()

def call_procedure_add_phone(conn):
    name = input("Contact Name: ")
    phone = input("Phone Number: ")
    ptype = input("Type (home/work/mobile): ").lower()
    if ptype not in ['home', 'work', 'mobile']:
        print("Invalid type. Defaulting to 'mobile'.")
        ptype = 'mobile'
        
    try:
        with conn.cursor() as cur:
            cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))
        conn.commit()
        print("\nPhone added successfully via procedure.")
    except Exception as e:
        print(f"\nError: {e}")
        conn.rollback()

def call_procedure_move_to_group(conn):
    name = input("Contact Name: ")
    group = input("Target Group Name: ")
    try:
        with conn.cursor() as cur:
            cur.execute("CALL move_to_group(%s, %s)", (name, group))
        conn.commit()
        print(f"\nContact '{name}' moved to group '{group}' via procedure.")
    except Exception as e:
        print(f"\nError: {e}")
        conn.rollback()

def call_function_search_contacts(conn):
    query = input("Enter search keyword (name, email, or phone): ")
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM search_contacts(%s)", (query,))
        results = cur.fetchall()
        print("\n--- Global Search Results ---")
        if not results:
            print("No matches found.")
        for r in results:
            print(f"Name: {r[0]}, Email: {r[1]}, Group: {r[2]}, Phone: {r[3]} ({r[4]})")

def main():
    conn = connect()
    if not conn:
        return

    while True:
        print("\n" + "="*30)
        print(" PhoneBook Advanced Menu ")
        print("="*30)
        print("1. Filter by Group")
        print("2. Search by Email")
        print("3. View Contacts (Paginated & Sorted)")
        print("4. Export to JSON")
        print("5. Import from JSON")
        print("6. Call Proc: Add Phone")
        print("7. Call Proc: Move to Group")
        print("8. Call Func: Global Search")
        print("9. Import from Extended CSV")
        print("0. Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == '1': filter_by_group(conn)
        elif choice == '2': search_by_email(conn)
        elif choice == '3': paginated_view(conn)
        elif choice == '4': export_to_json(conn)
        elif choice == '5': import_from_json(conn)
        elif choice == '6': call_procedure_add_phone(conn)
        elif choice == '7': call_procedure_move_to_group(conn)
        elif choice == '8': call_function_search_contacts(conn)
        elif choice == '9': import_from_csv(conn)
        elif choice == '0':
            print("Exiting PhoneBook. Goodbye!")
            conn.close()
            break
        else:
            print("Invalid choice. Please select a valid number.")

if __name__ == '__main__':
    main()