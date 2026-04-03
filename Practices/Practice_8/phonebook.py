import psycopg2
import csv

def get_connection():
    return psycopg2.connect(
        dbname="phonebook_db",
        user="postgres",
        password="",
        host="localhost",
        port="5432"
    )

def list_tables():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    tables = [t[0] for t in cur.fetchall()]
    if tables:
        print("Tables:", ", ".join(tables))
    else:
        print("No tables yet.")
    cur.close(); conn.close()
    return tables

# ✅ CREATE TABLE (сол күйі)
def create_table():
    name = input("Table name: ")
    query = f"CREATE TABLE IF NOT EXISTS {name} (name VARCHAR, phone VARCHAR);"
    conn = get_connection(); cur = conn.cursor()
    cur.execute(query); conn.commit()
    cur.close(); conn.close()
    print(f"Table '{name}' created!")

# ✅ ADD (процедура арқылы)
def add_contact():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Name: ")
    phone = input("Phone: ")

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("Added!")

# ✅ UPDATE (сол процедура)
def update_contact():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Enter name: ")
    phone = input("Enter new phone: ")

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("Updated!")

# ✅ FIND (function)
def find_contact():
    conn = get_connection()
    cur = conn.cursor()

    text = input("Search: ")

    cur.execute("SELECT * FROM search_contacts(%s)", (text,))
    rows = cur.fetchall()

    if not rows:
        print("No results")
    else:
        for r in rows:
            print(r)

    cur.close()
    conn.close()

# ✅ PAGINATION
def show_page():
    conn = get_connection()
    cur = conn.cursor()

    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    cur.execute("SELECT * FROM get_contacts(%s, %s)", (limit, offset))

    for r in cur.fetchall():
        print(r)

    cur.close()
    conn.close()

# ✅ DELETE (procedure)
def delete_contact():
    conn = get_connection()
    cur = conn.cursor()

    value = input("Enter name or phone to delete: ")

    cur.execute("CALL delete_contact(%s)", (value,))

    conn.commit()
    cur.close()
    conn.close()
    print("Deleted!")

# ✅ CSV (сол күйі)
def insert_csv():
    conn = get_connection()
    cur = conn.cursor()

    path = input("CSV path: ")

    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("CALL upsert_contact(%s, %s)", (row['name'], row['phone']))

    conn.commit()
    cur.close()
    conn.close()
    print("CSV inserted!")

# 🔥 MENU
while True:
    print("\n1.Create table")
    print("2.Add contact")
    print("3.Update contact")
    print("4.Find contact")
    print("5.Show page (pagination)")
    print("6.Delete contact")
    print("7.Insert CSV")
    print("8.List tables")
    print("9.Exit")

    choice = input("Choice: ")

    if choice == "1":
        create_table()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        find_contact()
    elif choice == "5":
        show_page()
    elif choice == "6":
        delete_contact()
    elif choice == "7":
        insert_csv()
    elif choice == "8":
        list_tables()
    elif choice == "9":
        break