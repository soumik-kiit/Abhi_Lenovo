import pyodbc

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
insert_query = "INSERT INTO OrdersDemo2 (name, number,  orders) VALUES (?, ?, ?)"
params = ('PythonVScode', '111', 'pizza')

# Execute the INSERT query with parameters
cursor.execute(insert_query, params)

# Commit the transaction to save the changes
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()