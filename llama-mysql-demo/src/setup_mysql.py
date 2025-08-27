import os
import subprocess
import mysql.connector
from mysql.connector import errorcode

def install_mysql():
    try:
        # Install MySQL server
        subprocess.run(['sudo', 'apt-get', 'install', 'mysql-server', '-y'], check=True)
        print("MySQL installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing MySQL: {e}")

def create_database_and_table():
    try:
        # Connect to MySQL server
        cnx = mysql.connector.connect(user='root', password='!23')
        cursor = cnx.cursor()

        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS test_db")
        print("Database 'test_db' created successfully.")

        # Use the created database
        cursor.execute("USE test_db")

        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        print("Table 'users' created successfully.")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    install_mysql()
    create_database_and_table()