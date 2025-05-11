from database import create_connection, create_table_if_not_exists
from data_operations import insert_rows, query_users, update_user_balance, delete_user, delete_table


def main():

    connection = create_connection()

    with connection:
        create_table_if_not_exists(connection)

        insert_rows(connection)

        query_users(connection)

        update_user_balance(connection, 1, 1000.0)

        delete_user(connection, 1)

        # delete_table(connection)


if __name__ == "__main__":
    main()
