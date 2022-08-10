import hashlib
import Database


def get_all():
    connection = Database.connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    found_users = cursor.fetchall()
    connection.close()
    return found_users


def add(first_name, last_name, master_password):
    try:
        connection = Database.connect()
        cursor = connection.cursor()
        encrypted_master_password = hashlib.sha256(
            master_password.encode("utf-8")
        ).hexdigest()
        cursor.execute(
            """
            INSERT INTO users
                (first_name, last_name, master_password)
                VALUES (?, ?, ?)
            """,
            (first_name, last_name, encrypted_master_password),
        )
        connection.commit()
        connection.close()
        return True
    except Database.Error as err:
        print("An error has occurred.")
        print(str(err))
        return False


def authenticate(master_password):
    try:
        connection = Database.connect()
        cursor = connection.cursor()
        encrypted_master_password = hashlib.sha256(
            master_password.encode("utf-8")
        ).hexdigest()
        cursor.execute(
            """
            SELECT * FROM users
                WHERE master_password=?
            """,
            (encrypted_master_password,),
        )
        found_users = cursor.fetchall()
        connection.close()
        return found_users
    except Database.Error as err:
        print("An error has occurred.")
        print(str(err))
        return []
