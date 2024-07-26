def admin_menu(connection):
    while True:
        print("1. Manage Inventory")
        print("2. Manage Users")
        print("3. View All Orders")
        print("4. Logout")
        choice = input("Enter choice: ")
        
        if choice == '4':
            break
     