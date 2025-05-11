# PostgreSQL with Python Example

This project demonstrates how to work with PostgreSQL in Python using the `psycopg2` library. It includes examples for creating tables, inserting data, querying, updating, and deleting entries in the database. The goal of this project is to showcase fundamental database operations and best practices when interacting with PostgreSQL through Python.

## Features

- Establish a secure connection to a PostgreSQL database using environment variables.
- Create a `users` table if it doesn't already exist.
- Insert multiple rows into the `users` table.
- Query users based on their balance.
- Update user balances.
- Delete a user from the database.
- Optionally, drop the `users` table.





## Requirements

- Python 3.6+
- PostgreSQL database

### Install Dependencies

To install the required Python libraries, use the following command:

```bash
pip install -r requirements.txt
```

Setting Up .env File
Create a .env file in the root directory of your project.

Add the following content to it:

```
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=12345
DB_HOST=127.0.0.1
DB_PORT=5432
```

Explanation of Files
database.py

This file contains functions to establish a connection to the PostgreSQL database and create the necessary tables.

data_operations.py

This file contains the functions for inserting, querying, updating, and deleting records in the users table.



main.py

This is the main script that orchestrates all database operations. It connects to the database and uses functions from database.py and data_operations.py.

README.md

This file explains how to set up and use the project.

.env

This file stores sensitive information such as database credentials. Make sure to keep this file secure and add it to .gitignore to prevent it from being uploaded to version control systems like Git.

Additional Features

Environment variables: All database configuration parameters are stored in a .env file to keep them secure and easily configurable across different environments (e.g., development, production).

Security: The project uses python-dotenv to load environment variables from the .env file, keeping sensitive information out of the source code.

Modular design: The code is divided into separate modules (database.py, data_operations.py), making it easy to extend or maintain.