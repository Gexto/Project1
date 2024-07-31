import mysql.connector

cnx = mysql.connector.connect(user='root', password='1234',
                              host='127.0.0.1',
                              database='myfirstdb')

cursor = cnx.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(10) NOT NULL,
    balance DECIMAL(10, 2) DEFAULT 0.00
)
"""
cursor.execute(create_table_query)

cnx.commit()
cursor.execute("SHOW TABLES")

print("Tables in the database:")
for table in cursor:
    print(table)

cursor.close()
cnx.close()

