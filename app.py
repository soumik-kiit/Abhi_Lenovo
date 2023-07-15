print ("Hello World")

from flask import Flask, jsonify
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app)

@app.route('/orders', methods=['GET'])
def get_orders():
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

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Convert the rows to a list of dictionaries
    orders = []
    for row in rows:
        order = {
            'id': row[0],
            'name': row[1],
            # Add more fields as needed
        }
        orders.append(order)

    return jsonify(orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
