print ("Hello World")

import pyodbc

server = 'relailer-order-demo.database.windows.net'
database = 'Retail_orders'
username = 'retailer_admin@relailer-order-demo'
password = 'asdzxc1234#'

# Establish the database connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a sample query
cursor.execute("SELECT * FROM OrdersDemo")
rows = cursor.fetchall()

# Process the fetched rows
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
