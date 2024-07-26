from db_operations import add_user

def login(connection):
    username = input("Username: ")
    password = input("Password: ")
    
    cursor = connection.cursor()
    query = "SELECT role FROM Users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    
    if result:
        return result[0]
    else:
        print("Invalid credentials")
        return None

def register(connection):
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    role = input("Enter role (user/admin): ")
    
    # Add input validation here if necessary
    
    add_user(connection, username, password, role)
    print("User registered successfully!")
