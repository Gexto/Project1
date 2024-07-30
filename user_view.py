from db_user_operations import view_shoes, purchase_shoes, view_order_history

def user_menu(connection, user_id):
    while True:
        print("\n1. View Shoes")
        print("2. Purchase Shoes")
        print("3. View Order History")
        print("4. Logout\n")
        choice = input("Enter choice: ")
        #=======================================================================================
        if choice == '1':
            shoes = view_shoes(connection)
            print("Available Shoes:")
            print("===============================================================================")
            for shoe in shoes:
                print(f"ID: {shoe[0]}, Brand: {shoe[1]}, Model: {shoe[2]}, Size: {shoe[3]}, Price: {shoe[4]}, Quantity: {shoe[5]}")
            print("===============================================================================")
        #=======================================================================================
        elif choice == '2':
            shoe_id = int(input("Enter shoe ID to purchase: "))
            quantity = int(input("Enter quantity: "))
            purchase_shoes(connection, user_id, shoe_id, quantity)
        #=======================================================================================
        elif choice == '3':
            orders = view_order_history(connection, user_id)
            print("Order History:")
            for order in orders:
                print(f"Order ID: {order[0]}, Date: {order[1]}, Total Amount: {order[2]}, Status: {order[3]}, Shoe ID: {order[4]}, Quantity: {order[5]}, Price: {order[6]}")
        #=======================================================================================
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")