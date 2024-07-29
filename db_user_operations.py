import logging

def add_user(connection, username, password, role):
    cursor = connection.cursor() #creates a cursor object to execute SQL commands
    add_user_query = "INSERT INTO Users (username, password, role) VALUES (%s, %s, %s)"
    cursor.execute(add_user_query, (username, password, role))

    connection.commit()
    logging.info(f"User {username} added with role {role}.")  #log user addition
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

    query = "SELECT price, quantity FROM Shoes WHERE shoe_id = %s" #defines a SQL query to check if the shoe exists and retrieve its price and quantity
    cursor.execute(query, (shoe_id,))
    shoe = cursor.fetchone()  #fetches the result of the query
    
    if shoe and shoe[1] >= quantity:    #Checks if the shoe exists and if theres enough quantity available for purchase
        price = shoe[0]                 #gets the price of the shoe
        total_amount = price * quantity #calculates the total amount for the purchase

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
def view_order_history(connection, user_id):
    cursor = connection.cursor()
    query = """
    SELECT Orders.order_id, Orders.order_date, Orders.total_amount, Orders.status,
           OrderItems.shoe_id, OrderItems.quantity, OrderItems.price
    FROM Orders
    JOIN OrderItems ON Orders.order_id = OrderItems.order_id
    WHERE Orders.user_id = %s
    ORDER BY Orders.order_date DESC
    """
    cursor.execute(query, (user_id,))
    orders = cursor.fetchall() #fetches all rows from the executed query
    cursor.close()
    return orders