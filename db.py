import mysql.connector

# Connect to MySQL database
try:
    conn = mysql.connector.connect(
        host="mysqldba",
        user="root",
        password="root",
        database="akshansh"
    )
    print("Connected to MySQL database")
except mysql.connector.Error as err:
    print("Error connecting to MySQL database:", err)
    exit(1)

# Function to read data from the 'name' table
def read_data():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM name")
        rows = cursor.fetchall()
        print("Data from 'name' table:")
        for row in rows:
            print(row[0])
    except mysql.connector.Error as err:
        print("Error reading data from 'name' table:", err)
    finally:
        cursor.close()

# Function to insert data into the 'name' table
def insert_data(name):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO name (name) VALUES (%s)"
        cursor.execute(query, (name,))
        conn.commit()
        print("Inserted data into 'name' table successfully")
    except mysql.connector.Error as err:
        print("Error inserting data into 'name' table:", err)
        conn.rollback()
    finally:
        cursor.close()

# Main function
def main():
    # Read data from 'name' table
    # read_data()
    test =input('enter y to add name to list :: ')
    if test:
        name=input('enter your name :: ')
        insert_data(name)
    # Read data again after insertion
    read_data()

# Execute main function
if __name__ == "__main__":
    main()

# Close MySQL connection
conn.close()
