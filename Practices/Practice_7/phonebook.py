import psycopg2
import csv

def get_connection():
    return psycopg2.connect(dbname="phonebook_db", user="postgres", password="", host="localhost", port="5432")

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

def create_table():
    name = input("Table name: ")
    query = f"CREATE TABLE IF NOT EXISTS {name} ();"
    conn = get_connection(); cur = conn.cursor()
    cur.execute(query); conn.commit()
    cur.close(); conn.close()
    print(f"Table '{name}' created!")

def add_column():
    tables = list_tables()
    tname = input("Table to add column: ")
    if tname not in tables: return
    conn = get_connection(); cur = conn.cursor()
    col = input("Column name: ")
    ctype = input("Type (VARCHAR(255), INT...): ")
    cur.execute(f"ALTER TABLE {tname} ADD COLUMN IF NOT EXISTS {col} {ctype};")
    conn.commit(); cur.close(); conn.close()
    print(f"Column '{col}' added!")

def add_row():
    tables = list_tables()
    tname = input("Table to add row: ")
    if tname not in tables: return
    conn = get_connection(); cur = conn.cursor()
    cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name='{tname}';")
    cols = [c[0] for c in cur.fetchall()]
    vals = [input(f"{c}: ") for c in cols]
    cur.execute(f"INSERT INTO {tname} ({', '.join(cols)}) VALUES ({', '.join(['%s']*len(cols))});", vals)
    conn.commit(); cur.close(); conn.close()
    print("Row added!")

def update_contact():
    tables = list_tables()
    tname = input("Table to update: ")
    conn = get_connection(); cur = conn.cursor()
    cur.execute(f"SELECT * FROM {tname};")
    rows = cur.fetchall()
    for i, r in enumerate(rows, 1): print(i, r)
    row_num = int(input("Row number to update: "))
    col = input("Column to update: ")
    new_val = input("New value: ")
    row_data = rows[row_num-1]
    identifier_col = cur.description[0].name
    identifier_val = row_data[0]
    cur.execute(f"UPDATE {tname} SET {col}=%s WHERE {identifier_col}=%s;", (new_val, identifier_val))
    conn.commit(); cur.close(); conn.close()
    print("Contact updated!")

def find_contact():
    tables = list_tables()
    tname = input("Table to search: ")
    conn = get_connection(); cur = conn.cursor()
    col = input("Column to search in: ")
    val = input("Search value: ")
    cur.execute(f"SELECT * FROM {tname} WHERE {col} ILIKE %s;", (f"%{val}%",))
    for r in cur.fetchall(): print(r)
    cur.close(); conn.close()

def insert_csv():
    tables = list_tables()
    tname = input("Table for CSV: ")
    conn = get_connection(); cur = conn.cursor()
    cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name='{tname}';")
    cols = [c[0] for c in cur.fetchall()]
    path = input("CSV path: ")
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            c = [col for col in cols if col in row]
            v = [row[col] for col in c]
            cur.execute(f"INSERT INTO {tname} ({', '.join(c)}) VALUES ({', '.join(['%s']*len(v))});", v)
    conn.commit(); cur.close(); conn.close()
    print("CSV inserted!")

# Menu
while True:
    print("1.Create table \n2.Add column \n3.Add row \n4.Update \n5.Find \n6.Insert CSV \n7.List tables \n8.Exit")
    choice = input("Choice: ")
    if choice=="1": create_table()
    elif choice=="2": add_column()
    elif choice=="3": add_row()
    elif choice=="4": update_contact()
    elif choice=="5": find_contact()
    elif choice=="6": insert_csv()
    elif choice=="7": list_tables()
    elif choice=="8": break