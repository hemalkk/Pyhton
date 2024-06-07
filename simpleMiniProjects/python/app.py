from flask import Flask, render_template  # Import Flask and render_template from the flask module
import mysql.connector  # Import the mysql.connector module to interact with the MySQL database

# Initialize the Flask application
app = Flask(__name__)

# Database connection configuration
db_connection = {
    'user': 'root',       # MySQL username
    'password': '',       # MySQL password 
    'host': 'localhost',  # Host Name
    'database': 'python'  # Database Name
}

# Fetch data from the database
def get_data():
    try:
        #Connect database
        conn = mysql.connector.connect(**db_connection)
        cursor = conn.cursor()

        # Execute a SQL query to fetch all rows from the 'users' table
        cursor.execute("SELECT * FROM users")

        # Fetch all rows from the executed query
        rows = cursor.fetchall()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

        # Return the fetched rows
        return rows
    except mysql.connector.Error as err:
        # Print any error that occurs and return an empty list
        print(f"Error: {err}")
        return []

# Define the route for the home page
@app.route('/')
def index():
    # Fetch data from the database
    data = get_data()
    # Render the 'index.html' template, passing the fetched data to it
    return render_template('index.html', data=data)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=7882)  # Start the Flask app with debug mode on and specify the port number
