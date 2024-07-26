from db_connection import create_connection
from user_view import user_menu
from admin_view import admin_menu
from auth_controller import login

def main():
    connection = create_connection()
    
    #user login
    role = login(connection)
    
    if role == 'user':
        user_menu(connection)
    elif role == 'admin':
        admin_menu(connection)

    connection.close()

if __name__ == '__main__':
    main()
