from db_admin_operations import manage_inventory, manage_users, view_all_orders

def admin_menu(connection):
    while True:
        print("1. Manage Inventory")
        print("2. Manage Users")
        print("3. View All Orders")
        print("4. Logout")
        choice = input("Enter choice: ")
        
        if choice == '1':
            manage_inventory(connection)
        elif choice == '2':
            manage_users(connection)
        elif choice == '3':
            view_all_orders(connection)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")