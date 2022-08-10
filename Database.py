import sqlite3


Error = sqlite3.Error


def connect():
    try:
        connection = sqlite3.connect("database.db")
        return connection
    except Error as err:
        print("An error has occurred.")
        print(str(err))


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            master_password TEXT NOT NULL
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL, 
            url TEXT NOT NULL, 
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            description TEXT
        )
        """
    )
    connection.commit()
