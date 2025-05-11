def insert_sample_users(conn):
    with conn.cursor() as cursor:
        query = """
        INSERT INTO users (first_name, last_name, age, height, weight, balance)
        VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;
        """
        users = [
            ('John', 'Doe', 25, 6.0, 180.0, 2000.5),
            ('Jane', 'Smith', 30, 5.5, 150.0, 3400.0),
            ('Alice', 'Johnson', 22, 5.8, 160.0, 1200.0),
            ('Bob', 'Williams', 28, 6.2, 200.0, 4500.0),
            ('Eve', 'Brown', 35, 5.6, 170.0, 5100.0),
        ]
        for user in users:
            cursor.execute(query, user)
            print("Inserted ID:", cursor.fetchone()[0])
        conn.commit()

def get_wealthy_users(conn, min_balance=3000.0):
    with conn.cursor() as cursor:
        cursor.execute("""
        SELECT id, first_name, last_name, balance
        FROM users
        WHERE balance > %s
        ORDER BY balance DESC;
        """, (min_balance,))
        return cursor.fetchall()

def update_user_balance(conn, user_id, new_balance):
    with conn.cursor() as cursor:
        cursor.execute("""
        UPDATE users
        SET balance = %s, updated_at = CURRENT_TIMESTAMP
        WHERE id = %s;
        """, (new_balance, user_id))
        conn.commit()

def delete_user(conn, user_id):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
        conn.commit()
