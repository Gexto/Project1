from db_connection import create_connection
from user_view import user_menu
from admin_view import admin_menu
from auth_controller import login, register

from logger import setup_logging

def main():
    setup_logging()
    connection = create_connection()
    
    while True:
        print("1. Login")
        print("2. Register")
        choice = input("Enter choice: ")
        
        if choice == '1':
            user_id, role = login(connection)
            if role == 'user':
                user_menu(connection, user_id)
            elif role == 'admin':
                admin_menu(connection)
        elif choice == '2':
            register(connection)
        else:
            print("Invalid choice, please try again.")
    
    connection.close()

if __name__ == '__main__':
    main()
