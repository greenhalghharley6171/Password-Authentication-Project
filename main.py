import sqlite3

def database_connection():
    connection = sqlite3.connect("Password data.db")
    cursor = connection.cursor()
    return connection , cursor

def menu_choice():
    choices = [1,2,3]
    flag = True

    while flag:
        try:
            print("1. Exit")
            print("2. Create Account")
            print("3. Login")
            user_choice = int(input("Please enter your menu choice: "))
            if user_choice > len(choices):
                print(f"Please ensure the number you have entered is lower than or equal to {len(choices)}")
            elif user_choice < choices[0]:
                print(f"Please ensure the number you have entered is higher than or equal to {choices[0]}")
            else:
                return user_choice
        except:
            print("Please enter your choice as a whole number")

def get_username(cursor, locked_accounts):
    flag = True

    while flag:
        username = input("Please enter a username: ").strip()
        if username in locked_accounts:
            print("This accounts is locked, please try another username")
        else:
            cursor.execute("SELECT * FROM User_tbl WHERE Username=?",(username,))
            user = cursor.fetchone()
            if user:
                break
            else:
                print("This username does not exist")
    return username
    
def get_password(cursor, username, locked_accounts, logged_in):
    flag = True
    attempts = 3

    while flag:
        password = input("Please enter a password: ").strip()
        cursor.execute("SELECT * FROM User_tbl WHERE Password=? AND Username=?",(password,username))
        user = cursor.fetchone()
        if user:
            print("Login successful")
            logged_in = True
            break
        else:
            attempts -= 1
            if attempts < 1:
                print(f"The account {username} is now locked")
                locked_accounts.append(username)
                logged_in = False
                break
            else:
                print(f"Login failed, you have {attempts} attempts remaining")

    return logged_in , locked_accounts
            
def check_login(cursor): 
    logged_in = False 
    locked_accounts = []

    while not logged_in:
        username = get_username(cursor, locked_accounts)
        logged_in , locked_accounts = get_password(cursor, username, locked_accounts, logged_in)

def create_username(cursor):
    flag = True
    while flag:
        username = input("Please enter a username: ").strip()
        if username == "":
            print("Usernames can not be left blank")
        elif len(username) > 12:
            print("Usernames can not be more than 12 characters")
        else:
            cursor.execute("SELECT * FROM User_tbl WHERE Username=?",(username,))
            user = cursor.fetchone()
            if user:
                print("This username is already in use")
            else:
                break
    return username

def create_password():
    flag = True 

    while flag:
        has_upper = False
        has_digit = False 
        password = input("Please enter your password: ")
        if len(password) < 8:
            print("The password must be atleast 8 characters long")
        else:
            for char in password:
                if char.isupper():
                    has_upper = True
                    break
            if has_upper == False:
                print("The password must contain atleast 1 uppercase")
            else:
                for char in password:
                    if char.isdigit():
                        has_digit = True
                        break
                if has_digit == False:
                    print("The password must contain atleast 1 number")
                else:
                    break
    return password

def create_account(cursor , connection):
    username = create_username(cursor)
    password = create_password()
    cursor.execute("INSERT INTO User_tbl (Username , Password) VALUES (?,?)",(username,password))
    connection.commit()
    print("Account create successfully!")
    
def main():
    flag = True
    connection , cursor = database_connection()
    while flag:
        user_choice = menu_choice()
        if user_choice == 1:
            connection.close()
            print("Goodbye!")
            quit()
        elif user_choice == 2:
            create_account(cursor , connection)
        elif user_choice == 3:
            check_login(cursor)
              
main()