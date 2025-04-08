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
            balance REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor.execute(create_table_query)
        conn.commit()


def insert_rows(conn):
    with conn.cursor() as cursor:
        insert_query = """
        INSERT INTO users (first_name, last_name, age, height, weight, balance)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id;
        """
        rows = [
            ('John', 'Doe', 25, 6.0, 180.0, 2000.5),
            ('Jane', 'Smith', 30, 5.5, 150.0, 3400.0),
            ('Alice', 'Johnson', 22, 5.8, 160.0, 1200.0),
            ('Bob', 'Williams', 28, 6.2, 200.0, 4500.0),
            ('Eve', 'Brown', 35, 5.6, 170.0, 5100.0),
        ]
        inserted_ids = []
        for row in rows:
            cursor.execute(insert_query, row)
            inserted_id = cursor.fetchone()[0]  # Получить первый (и единственный) результат
            inserted_ids.append(inserted_id)  # Сохранить ID
        conn.commit()
        print("Inserted row IDs:", inserted_ids)


def query_users(conn):
    with conn.cursor() as cursor:
        query = """
        SELECT id, first_name, last_name, age, height, weight, balance, created_at
        FROM users
        WHERE balance > %s
        ORDER BY balance DESC;
        """
        cursor.execute(query, (3000.0,))
        results = cursor.fetchall()
        for row in results:
            print(row)


def update_user_balance(conn, user_id, new_balance):
    with conn.cursor() as cursor:
        update_query = """
        UPDATE users
        SET balance = %s, updated_at = CURRENT_TIMESTAMP
        WHERE id = %s;
        """
        cursor.execute(update_query, (new_balance, user_id))
        conn.commit()


def delete_user(conn, user_id):
    with conn.cursor() as cursor:
        delete_query = """
        DELETE FROM users
        WHERE id = %s;
        """
        cursor.execute(delete_query, (user_id,))
        conn.commit()


def delete_table(conn):
    with conn.cursor() as cursor:
        delete_all = """
        DROP TABLE users;
        """
        cursor.execute(delete_all)
        conn.commit()


connection = create_connection()


with connection:
    create_table_if_not_exists(connection)
    insert_rows(connection)
    query_users(connection)
    update_user_balance(connection, 1, 1000.0)
    delete_user(connection, 1)
    #delete_table(connection)

