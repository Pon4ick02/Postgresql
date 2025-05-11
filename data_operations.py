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
            inserted_id = cursor.fetchone()[0]
            inserted_ids.append(inserted_id)
        conn.commit()
        print("added ID:", inserted_ids)

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
        print("users with balanse more than 3000:")
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
        print(f"updated balance ID {user_id} to {new_balance}")

def delete_user(conn, user_id):

    with conn.cursor() as cursor:
        delete_query = """
        DELETE FROM users
        WHERE id = %s;
        """
        cursor.execute(delete_query, (user_id,))
        conn.commit()
        print(f"User with ID {user_id} was deleted")

def delete_table(conn):

    with conn.cursor() as cursor:
        delete_all = """
        DROP TABLE IF EXISTS users;
        """
        cursor.execute(delete_all)
        conn.commit()
        print("table 'users' deleted.")
