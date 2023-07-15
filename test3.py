print ("Hello World")

import mysql.connector

# Database connection details
hostname = "localhost"
port = 3306
username = "root"
password = "asdzxc1234"
schema = "new_schema"

# Establishing a connection
try:
    connection = mysql.connector.connect(
        host=hostname,
        port=port,
        user=username,
        password=password,
        database=schema
    )
    print("Connected to the MySQL database!")

    # Creating a cursor object
    cursor = connection.cursor()

    # Executing the SELECT * query
    query = "SELECT * FROM orders"
    cursor.execute(query)

    # Fetching all rows from the result
    rows = cursor.fetchall()

    # Displaying the rows
    for row in rows:
        print(row)

    # Closing the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")
except mysql.connector.Error as error:
    print("Failed to connect to the MySQL database: {}".format(error))
