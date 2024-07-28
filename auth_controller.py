from db_user_operations import add_user

import logging

def login(connection):
    username = input("Username: ")
    password = input("Password: ")
    
    cursor = connection.cursor()
    query = "SELECT user_id, role FROM Users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    
    if result:
        user_id, role = result
        logging.info(f"User {username} logged in as {role}.") #log login is successful
        return user_id, role
    else:
        logging.warning(f"Failed login attempt for username: {username}.") #log failed login
        print("Invalid credentials")
        return None, None

def register(connection):
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    role = input("Enter role (user/admin): ")
    
    add_user(connection, username, password, role)
    print("User registered successfully!")
