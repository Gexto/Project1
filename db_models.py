def create_users_table(cursor):
    create_table_query = """
    CREATE TABLE Users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(255) NOT NULL,
        role VARCHAR(10) NOT NULL
    )
    """
    cursor.execute(create_table_query)

def create_shoes_table(cursor):
    create_table_query = """
    CREATE TABLE Shoes (
        shoe_id INT AUTO_INCREMENT PRIMARY KEY,
        brand VARCHAR(50) NOT NULL,
        model VARCHAR(50) NOT NULL,
        size DECIMAL(3, 1) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        quantity INT NOT NULL
    )
    """
    cursor.execute(create_table_query)

def create_orders_table(cursor):
    create_table_query = """
    CREATE TABLE Orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        total_amount DECIMAL(10, 2) NOT NULL,
        status VARCHAR(20) DEFAULT 'pending',
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    )
    """
    cursor.execute(create_table_query)

def create_order_items_table(cursor):
    create_table_query = """
    CREATE TABLE OrderItems (
        order_item_id INT AUTO_INCREMENT PRIMARY KEY,
        order_id INT,
        shoe_id INT,
        quantity INT NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (order_id) REFERENCES Orders(order_id),
        FOREIGN KEY (shoe_id) REFERENCES Shoes(shoe_id)
    )
    """
    cursor.execute(create_table_query)
