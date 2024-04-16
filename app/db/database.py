import mysql.connector
from db.database_config import DB_CONFIG


def create_database_users():
    try:
        # Establishing a connection to MySQL server
        connection = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
        )

        # Creating a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Defining the SQL query to check if the database exists
        check_db_query = f"SHOW DATABASES LIKE '{DB_CONFIG['database']}'"

        # Executing the SQL query to check if the database exists
        cursor.execute(check_db_query)

        result = cursor.fetchone()

        if result:
            print("Database already exists.")
            return

        # Defining the SQL query to create the database if it doesn't exist
        create_db_query = f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}"

        # Executing the SQL query to create the database
        cursor.execute(create_db_query)
        print("Database created successfully.")

    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")


# Calling the function to create the database
create_database_users()

# Establishing connection to the MySQL database
try:
    mydb = mysql.connector.connect(
        host=DB_CONFIG["host"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
    )

    mycursor = mydb.cursor()

    def create_user_table():
        try:
            # Defining SQL query to check if the users table already exists
            check_table_query = "SHOW TABLES LIKE 'users'"

            # Executing the SQL query to check if the table exists
            mycursor.execute(check_table_query)

            result = mycursor.fetchone()

            # create table if it doesn't exist
            if not result:
                create_table_query = """
                CREATE TABLE users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) NOT NULL UNIQUE,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL
                );
                """

                # Executing the SQL query to create the users table
                mycursor.execute(create_table_query)

                # Commit the transaction
                mydb.commit()
                print("Table 'users' created successfully.")
            else:
                print("Table 'users' already exists.")

        except mysql.connector.Error as err:
            print(f"An error occurred while creating the table: {err}")

    # Call the function to create the user table
    create_user_table()

except mysql.connector.Error as err:
    print(f"An error occurred while connecting to the database: {err}")
