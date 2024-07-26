def login(connection):
    #login
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
