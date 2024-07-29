from db_connection import create_connection
from db_models import create_users_table, create_shoes_table, create_orders_table, create_order_items_table

def initialize_database():
    connection = create_connection()
    cursor = connection.cursor() #create a cursor object to execute sql queries

    #calls functions to create the tables in the database
    create_users_table(cursor)
    create_shoes_table(cursor)
    create_orders_table(cursor)
    create_order_items_table(cursor)

    connection.commit()
    cursor.close() #close the cursor to free up resources
    connection.close()

if __name__ == '__main__':
    initialize_database()
    print("Database initialized successfully.")
