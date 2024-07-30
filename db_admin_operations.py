import logging

def manage_inventory(connection):
    cursor = connection.cursor()

    while True:
        print("\n1. Add Shoe")
        print("2. Update Shoe")
        print("3. Delete Shoe")
        print("4. View All Shoes")
        print("5. Back to Admin Menu\n")
        choice = input("Enter choice: ")

        if choice == '1':
            brand = input("Enter brand: ")
            model = input("Enter model: ")
            size = float(input("Enter size: "))
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            add_shoe_query = "INSERT INTO Shoes (brand, model, size, price, quantity) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(add_shoe_query, (brand, model, size, price, quantity))
            connection.commit()
            print("Shoe added successfully!")

        elif choice == '2':
            shoe_id = int(input("Enter shoe ID to update: "))
            brand = input("Enter new brand: ")
            model = input("Enter new model: ")
            size = float(input("Enter new size: "))
            price = float(input("Enter new price: "))
            quantity = int(input("Enter new quantity: "))
            update_shoe_query = "UPDATE Shoes SET brand=%s, model=%s, size=%s, price=%s, quantity=%s WHERE shoe_id=%s"
            cursor.execute(update_shoe_query, (brand, model, size, price, quantity, shoe_id))
            connection.commit()
            print("Shoe updated successfully!")

        elif choice == '3':
            shoe_id = int(input("Enter shoe ID to delete: "))
            delete_shoe_query = "DELETE FROM Shoes WHERE shoe_id=%s"
            cursor.execute(delete_shoe_query, (shoe_id,))
            connection.commit()
            print("Shoe deleted successfully!")

        elif choice == '4':
            view_shoes_query = "SELECT * FROM Shoes"
            cursor.execute(view_shoes_query)
            shoes = cursor.fetchall() #fetches all rows from the result set of the executed query and stores them in the 'shoes' variable as a list of tuples.
            print("All Shoes:")
            print("===============================================================================")
            for shoe in shoes:
                print(f"ID: {shoe[0]}, Brand: {shoe[1]}, Model: {shoe[2]}, Size: {shoe[3]}, Price: {shoe[4]}, Quantity: {shoe[5]}")
            print("===============================================================================")
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")
    
    cursor.close()

#================================================================================================================    
def manage_users(connection):
    cursor = connection.cursor()

    while True:
        print("\n1. Add User")
        print("2. Update User")
        print("3. Delete User")
        print("4. View All Users")
        print("5. Back to Admin Menu\n")
        choice = input("Enter choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (user/admin): ")
            add_user_query = "INSERT INTO Users (username, password, role) VALUES (%s, %s, %s)"
            cursor.execute(add_user_query, (username, password, role))
            connection.commit()
            print("User added successfully!")

        elif choice == '2':
            user_id = int(input("Enter user ID to update: "))
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            role = input("Enter new role (user/admin): ")
            update_user_query = "UPDATE Users SET username=%s, password=%s, role=%s WHERE user_id=%s"
            cursor.execute(update_user_query, (username, password, role, user_id))
            connection.commit()
            print("User updated successfully!")

        elif choice == '3':
            user_id = int(input("Enter user ID to delete: "))
            delete_user_query = "DELETE FROM Users WHERE user_id=%s"
            cursor.execute(delete_user_query, (user_id,))
            connection.commit()

            logging.info(f"User with the Id {user_id} deleted from database") #log deleted username
            print("User deleted successfully!")

        elif choice == '4':
            view_users_query = "SELECT * FROM Users"
            cursor.execute(view_users_query)
            users = cursor.fetchall()
            print("All Users:")
            print("===============================================================================")
            for user in users:
                print(f"ID: {user[0]}, Username: {user[1]}, Role: {user[3]}")
            print("===============================================================================")
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")
    
    cursor.close()

#===============================================================================================================

def view_all_orders(connection):
    cursor = connection.cursor()
    query = """
    SELECT Orders.order_id, Orders.user_id, Orders.order_date, Orders.total_amount, Orders.status,
           OrderItems.shoe_id, OrderItems.quantity, OrderItems.price
    FROM Orders
    JOIN OrderItems ON Orders.order_id = OrderItems.order_id
    ORDER BY Orders.order_date DESC
    """
    cursor.execute(query)
    orders = cursor.fetchall()
    cursor.close()

    print("All Orders:")
    print("===============================================================================")
    for order in orders:
        print(f"Order ID: {order[0]}, User ID: {order[1]}, Date: {order[2]}, Total Amount: {order[3]}, Status: {order[4]}, Shoe ID: {order[5]}, Quantity: {order[6]}, Price: {order[7]}")
    print("===============================================================================")