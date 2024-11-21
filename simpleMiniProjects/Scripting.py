import mysql.connector
import json

# Database connection details
db_config = {
    "host": "sql12.freesqldatabase.com",       # Database host
    "user": "sql12746404",                     # Database username
    "password": "lrmtWx3KSQ",                  # Database password
    "database": "sql12746404",                 # Database name
}

def insert_json_to_database(json_file_path, db_config):
    """
    Function to read data from a JSON file and insert it into a MySQL database.

    Parameters:
    - json_file_path: Path to the JSON file containing data.
    - db_config: Dictionary containing database connection details.
    """
    try:
        # Establish connection to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Define the SQL query for inserting data
        insert_query = "INSERT INTO employee (name, age, city) VALUES (%s, %s, %s)"

        # Read the JSON file
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        # Iterate through each record in the JSON file
        for user in data:
            # Extract user details with default values for missing fields
            name = user.get('name', 'N/A')
            age = user.get('age', 0)  # Default age is 0 if missing
            city = user.get('city', 'N/A')

            # Execute the INSERT query with the extracted data
            cursor.execute(insert_query, (name, age, city))

        # Commit the transaction to save changes in the database
        conn.commit()
        print(f"{cursor.rowcount} records inserted successfully.")

    except mysql.connector.Error as err:
        # Handle any database connection or execution errors
        print(f"Database Error: {err}")

    finally:
        # Ensure the database connection is properly closed
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Database connection closed.")

# Specify the path to the JSON file
json_file_path = 'users_1K.json'

# Call the function to insert data into the database
insert_json_to_database(json_file_path, db_config)
