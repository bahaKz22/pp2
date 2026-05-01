import psycopg2
from config import DB_CONFIG

def connect():
    try:
        print("Connecting to the PostgreSQL database...")
        # Передаем словарь DB_CONFIG с помощью распаковки **
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error connecting to database: {error}")
        return None