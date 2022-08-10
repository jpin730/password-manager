import Database


def get_all():
    try:
        connection = Database.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM passwords")
        found_passwords = cursor.fetchall()
        connection.close()
        return found_passwords
    except Database.Error as err:
        print("An error has occurred.")
        print(str(err))
        return []


def find(id):
    try:
        connection = Database.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM passwords WHERE id=?", (id,))
        found_passwords = cursor.fetchall()
        connection.close()
        return found_passwords
    except Database.Error as err:
        print("An error has occurred.")
        print(str(err))
        return []


def add(name, url, username, password, description):
    try:
        connection = Database.connect()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO passwords
                (name, url, username, password, description)
                VALUES (?, ?, ?, ?, ?)""",
            (name, url, username, password, description),
        )
        connection.commit()
        connection.close()
        print("Password added.")
    except Database.Error as err:
        print("An error has occurred.")
        print(str(err))


def edit(id, username, password):
    try:
        connection = Database.connect()
        cursor = connection.cursor()
        cursor.execute(
            """
            UPDATE passwords
                SET username = ?,
                    password = ?
                WHERE id = ?
            """,
            (username, password, id),
        )
        connection.commit()
        connection.close()
        print("Password edited.")
    except Database.Error as err:
        print("An error has occurred.")
        print(str(err))


def delete(id):
    try:
        connection = Database.connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM passwords WHERE id=?", (id,))
        connection.commit()
        connection.close()
        print("Password deleted.")
    except Database.Error as err:
        print("An error has occurred.")
        print(str(err))
