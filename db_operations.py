def add_user(connection, username, password, role):
    cursor = connection.cursor()
    add_user_query = "INSERT INTO Users (username, password, role) VALUES (%s, %s, %s)"
    cursor.execute(add_user_query, (username, password, role))
    connection.commit()
    cursor.close()

#User-options functions
#================================================================================================
def view_shoes(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM Shoes"
    cursor.execute(query)
    shoes = cursor.fetchall()
    cursor.close()
    return shoes
#------------------------------------------------------------------------------------------------
def purchase_shoes(connection, user_id, shoe_id, quantity):
    cursor = connection.cursor()

    #Check if the shoe exists and has enough quantity
    query = "SELECT price, quantity FROM Shoes WHERE shoe_id = %s"
    cursor.execute(query, (shoe_id,))
    shoe = cursor.fetchone()
    
    if shoe and shoe[1] >= quantity:
        price = shoe[0]
        total_amount = price * quantity

        #Insert into Orders table
        order_query = "INSERT INTO Orders (user_id, total_amount) VALUES (%s, %s)"
        cursor.execute(order_query, (user_id, total_amount))
        order_id = cursor.lastrowid

        #Insert into OrderItems table
        order_item_query = "INSERT INTO OrderItems (order_id, shoe_id, quantity, price) VALUES (%s, %s, %s, %s)"
        cursor.execute(order_item_query, (order_id, shoe_id, quantity, price))

        #Update the shoe quantity
        update_shoe_query = "UPDATE Shoes SET quantity = quantity - %s WHERE shoe_id = %s"
        cursor.execute(update_shoe_query, (quantity, shoe_id))

        connection.commit()
        print("Purchase successful!")
    else:
        print("Shoe not available or insufficient quantity.")

    cursor.close()
#------------------------------------------------------------------------------------------------