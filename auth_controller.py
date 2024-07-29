from db_user_operations import add_user

import logging

#this is how to verify someone's login credintials
def login(connection):
    username = input("Username: ")
    password = input("Password: ")
    
    cursor = connection.cursor()
    query = "SELECT user_id, role FROM Users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
        
    #checks if a matching user was found
    if result:
        user_id, role = result #retrieves user ID and role from the result
        logging.info(f"User {username} logged in as {role}.") #log login is successful
        return user_id, role
    else:
        logging.warning(f"Failed login attempt for username: {username}.") #log failed login
        print("Invalid credentials")
        return None, None #returns None for user ID and role if login fails

#how to refister a new person
def register(connection):
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    role = input("Enter role (user/admin): ")
    
    add_user(connection, username, password, role)
    print("User registered successfully!")
