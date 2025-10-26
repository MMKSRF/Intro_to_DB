#!/usr/bin/env python3
"""
MySQLServer.py
Creates the 'alx_book_store' database if it does not already exist.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update user/password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # 🔹 Replace with your actual MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection safely
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
