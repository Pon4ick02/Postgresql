import psycopg2
from psycopg2 import sql

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "12345"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"


def create_connection():
    return psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )


def create_table_if_not_exists(conn):
    with conn.cursor() as cursor:
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            age INTEGER NOT NULL,
            height REAL NOT NULL,
            weight REAL NOT NULL,
            balance REAL NOT NULL
        );
        """
        cursor.execute(create_table_query)
        conn.commit()


def insert_rows(conn):
    with conn.cursor() as cursor:
        insert_query = """
        INSERT INTO users (first_name, last_name, age, height, weight, balance)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        rows = [
            ('John', 'Doe', 25, 6.0, 180.0, 2000.5),
            ('Jane', 'Smith', 30, 5.5, 150.0, 3400.0),
            ('Alice', 'Johnson', 22, 5.8, 160.0, 1200.0),
            ('Bob', 'Williams', 28, 6.2, 200.0, 4500.0),
            ('Eve', 'Brown', 35, 5.6, 170.0, 5100.0),
        ]
        cursor.executemany(insert_query, rows)
        conn.commit()


connection = create_connection()

with connection:
    create_table_if_not_exists(connection)
    insert_rows(connection)

