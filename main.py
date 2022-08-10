import os
from getpass import getpass
from tabulate import tabulate
import Database
import User
import Password


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main():
    clear_screen()

    create_new_user = input("Do you want to create a new user? (y/N): ")
    if create_new_user.lower() == "y" and os.path.exists("database.db"):
        os.remove("database.db")

    clear_screen()

    connection = Database.connect()
    Database.create_tables(connection)
    connection.close()

    users = User.get_all()

    if len(users) == 0:
        print("Welcome, register your information.")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        master_password = getpass("Master password: ")
        if User.add(first_name, last_name, master_password):
            menu(first_name, last_name)
    else:
        master_password = getpass("Master password: ")
        found_users = User.authenticate(master_password)
        if len(found_users) == 0:
            print("Incorrect password.")
        else:
            _, first_name, last_name, _ = found_users[0]
            menu(first_name, last_name)


def menu(first_name, last_name):
    show_menu = True

    while True:
        if show_menu:
            clear_screen()
            print(f"Welcome {first_name} {last_name}!")
            print("1. View all passwords.")
            print("2. Show a password.")
            print("3. Add a password.")
            print("4. Edit a password.")
            print("5. Delete a password.")
            print("6. Exit.")
            show_menu = False

        option = input("Choose an options from above: ")

        if option == "1":
            view_all_passwords()
            show_menu = True
            input("Press enter to continue.")
        elif option == "2":
            find_password()
            show_menu = True
            input("Press enter to continue.")
        elif option == "3":
            add_password()
            show_menu = True
            input("Press enter to continue.")
        elif option == "4":
            edit_password()
            show_menu = True
            input("Press enter to continue.")
        elif option == "5":
            delete_password()
            show_menu = True
            input("Press enter to continue.")
        elif option == "6":
            print("Bye!")
            break
        else:
            print("Invalid option. Try again.")


def view_all_passwords():
    passwords = Password.get_all()
    headers = ["id", "name", "url", "username", "password", "description"]
    hided_passwords = []
    for password in passwords:
        hided_password = list(password)
        hided_password[4] = "********"
        hided_passwords.append(hided_password)

    table = tabulate(hided_passwords, headers, tablefmt="fancy_grid")
    clear_screen()
    print("All Passwords.")
    print(table)


def find_password():
    master_password = getpass("Master password: ")
    if len(User.authenticate(master_password)) != 0:
        id = input("Enter the password id show: ")
        password = Password.find(id)
        clear_screen()
        if len(password) == 0:
            print("Password not found.")
        else:
            headers = ["id", "name", "url", "username", "password", "description"]
            tabla = tabulate(password, headers, tablefmt="fancy_grid")
            print("Found password.")
            print(tabla)
    else:
        print("Incorrect password")


def add_password():
    clear_screen()
    print("Add password.")
    name = input("Name: ")
    url = input("Url: ")
    username = input("Username: ")
    password = getpass("Password: ")
    description = input("Description: ")
    clear_screen()
    Password.add(name, url, username, password, description)


def edit_password():
    master_password = getpass("Master password: ")
    if len(User.authenticate(master_password)) != 0:
        id = input("Enter the password id to edit: ")
        username = input("New username: ")
        password = getpass("New password: ")
        clear_screen()
        Password.edit(id, username, password)
    else:
        print("Incorrect password")


def delete_password():
    master_password = getpass("Master password: ")
    if len(User.authenticate(master_password)) != 0:
        id = input("Enter the password id to delete: ")
        clear_screen()
        Password.delete(id)
    else:
        print("Incorrect password")


main()
