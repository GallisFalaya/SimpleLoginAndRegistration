# Login_and_registration.py - a simple application that allows the user to register and log into the application.
# The user base is loaded from the .json file.

import json
import string


def main():
    choice = print_menu()

    while choice != "0":
        if choice == "1":
            print("""
        --------------------
        |    Login menu    |
        --------------------
        """)
            check_login_and_password()

        elif choice == "2":
            print("""
        ---------------------
        | Registration menu |
        ---------------------
        """)
            add_new_user()

        else:
            print("Wrong number was entered.")

        choice = print_menu()

    save_json("data_base.json", users_database)
    print("\nThe application has been shut down. Goodbye!")
    input("Press any key to end the program.")


def add_new_user():
    print("You can stop the registration process at any time by typing the word 'Abort!'")

    print("The username should be 3 to 10 characters long.")
    user = input("Please enter username: ")

    while len(user) not in range(3, 11):
        print("\nThe given username has the wrong size.\n")
        user = input("Please enter username: ")

    while user in users_database:
        print("\nThe given username is already used. Please enter another one.\n")
        user = input("Please enter username: ")

    if user != 'Abort!':

        password = correctness_of_password(3, 10)

        if password != 'Abort!':
            name = input("Please enter your name: ")
            if name != 'Abort!':
                lastname = input("Please enter lastname: ")
                if lastname != 'Abort!':
                    users_database[user] = {'password': password, 'name': name, 'lastname': lastname}
                    print("New user entry has been completed successfully.")


def check_login_and_password():
    user = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if user in users_database and users_database[user]['password'] == password:
        inner_application(user)
    else:
        print("\nThe entered data is incorrect.")


def correctness_of_password(min_num_of_char, max_num_of_char):
    print(f"\nThe password should be {min_num_of_char} to {max_num_of_char} characters long. Additionally, it should"
          f"contain at least one\nlowercase letter, capital letters, a number and a special character")
    password = input("Please enter password: ")

    # Each element of the table corresponds to one type of the required characters in the password,
    # if such appears there, the value of its element will be changed to True.
    correct_password = [False, False, False, False]

    while True:
        if password == 'Abort!':
            break
        elif len(password) not in range(min_num_of_char, max_num_of_char + 1):
            print("\nThe given password has the wrong size.\n")
        else:
            for i in password:
                if i in string.ascii_lowercase:
                    correct_password[0] = True
                elif i in string.ascii_uppercase:
                    correct_password[1] = True
                elif i in string.digits:
                    correct_password[2] = True
                elif i in string.punctuation:
                    correct_password[3] = True

            if sum(correct_password) == 4:
                break
            else:
                print("\nThe password does not contain all the required characters.\n")

        correct_password = [False, False, False, False]
        password = input("Please enter password: ")

    return password


def inner_application(user):
    """
    An example of the appearance of the application after logging in to it. The user can view all his data or exit it.
    """

    choice = print_menu(2)

    while choice != '0':
        if choice == '1':
            print("""
\t-------------------------
\t|       Your data       |
\t-------------------------""")
            for key in users_database[user].keys():
                print("\t| {0:8} | {1:10} |".format(key, users_database[user][key]))
            else:
                print("\t-------------------------")

        else:
            print("Wrong number was entered.")

        choice = print_menu(2)

    print("\nYou have been logged out of the application.")


def load_json(file_name):
    with open(file_name, 'r') as file:
        users_databases = json.load(file)

    return users_databases


def print_menu(number=1):
    if number == 1:
        print("""
        --------------------
        | Application menu |
        --------------------
        | 1. Login         |
        | 2. Registration  |
        | 0. Exit          |
        --------------------
""")

    elif number == 2:
        print("""
        ----------------------
        |  Application menu  |
        ----------------------
        | 1. View your data  |
        | 0. Logout          |
        ----------------------   
         """)

    return input("Selected option: ")


def save_json(file_name, database):
    with open(file_name, 'w') as file:
        json.dump(database, file, indent=2)


if __name__ == '__main__':
    try:
        users_database = load_json("data_base.json")
    except FileNotFoundError as e:
        print(f"An error occurred: {e}")
        input("\nPress any key to end the program.")
    else:
        main()
