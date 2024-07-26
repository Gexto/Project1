def add_user(connection, username, password, role):
    cursor = connection.cursor()
    add_user_query = "INSERT INTO Users (username, password, role) VALUES (%s, %s, %s)"
    cursor.execute(add_user_query, (username, password, role))
    connection.commit()
    cursor.close()