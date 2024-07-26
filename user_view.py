def user_menu(connection):
    while True:
        print("1. View Shoes")
        print("2. Purchase Shoes")
        print("3. View Order History")
        print("4. Logout")
        choice = input("Enter choice: ")
        
        if choice == '4':
            break
        # Add more functionality as needed
