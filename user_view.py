from db_operations import view_shoes, purchase_shoes

def user_menu(connection):
    while True:
        print("1. View Shoes")
        print("2. Purchase Shoes")
        print("3. View Order History")
        print("4. Logout")
        choice = input("Enter choice: ")
        #=======================================================================================
        if choice == '1':
            shoes = view_shoes(connection)
            print("Available Shoes:")
            for shoe in shoes:
                print(f"ID: {shoe[0]}, Brand: {shoe[1]}, Model: {shoe[2]}, Size: {shoe[3]}, Price: {shoe[4]}, Quantity: {shoe[5]}")
        #=======================================================================================
        elif choice == '2':
            shoe_id = int(input("Enter shoe ID to purchase: "))
            quantity = int(input("Enter quantity: "))
            purchase_shoes(connection, user_id, shoe_id, quantity)
        #=======================================================================================
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")