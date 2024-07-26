def add_user(connection, username, password, role):
    cursor = connection.cursor()
    add_user_query = "INSERT INTO Users (username, password, role) VALUES (%s, %s, %s)"
    cursor.execute(add_user_query, (username, password, role))
    connection.commit()
    cursor.close()

#User options operations
#================================================================================================
def view_shoes(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM Shoes"
    cursor.execute(query)
    shoes = cursor.fetchall()
    cursor.close()
    return shoes