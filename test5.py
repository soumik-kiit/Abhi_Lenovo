from flask import Flask, request
import pyodbc

print ("Data")

app = Flask(__name__)

@app.route('/insert', methods=['POST'])
def insert_data():
    # Parse the request body to extract the required parameters
    data = request.get_json()
    name = data['name']
    phone_number = data['phone_number']
    user_type = data['user_type']

    # Your code for connecting to the database, executing the query, and committing the changes
    server = 'relailer-order-demo.database.windows.net'
    database = 'Retail_orders'
    username = 'retailer_admin@relailer-order-demo'
    password = 'asdzxc1234#'
    driver = '{ODBC Driver 18 for SQL Server}'  # This may vary depending on your system configuration

    connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no"

    # Establish a connection to the Azure SQL database
    connection = pyodbc.connect(connection_string)

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Define the INSERT query and parameters
    insert_query = "INSERT INTO OrdersDemo (name, phone_number, user_type, order_list, create_date) VALUES (?, ?, ?, NULL, GETDATE())"
    params = (name, phone_number, user_type)

    # Execute the INSERT query with parameters
    cursor.execute(insert_query, params)

    # Commit the transaction to save the changes
    connection.commit()

    # Close the cursor and the connection
    cursor.close()
    connection.close()

    return 'Data inserted successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
