import mysql.connector

def create_connection():
    DB_CONFIG = {
    'user': 'root',
    'password': '1234',
    'host': '127.0.0.1',
    'database': 'myfirstdb'}
    
    #establishes a connection to the MySQL database using the specified configuration and returns the connection object.
    connection = mysql.connector.connect(**DB_CONFIG)
    return connection
