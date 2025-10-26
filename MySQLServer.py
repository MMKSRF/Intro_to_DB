#!/usr/bin/env python3
"""
MySQLServer.py
Creates the 'alx_book_store' database if it does not already exist.
"""

import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (update user/password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # 🔹 Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # Ensure connection is closed
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
        except NameError:
            # Connection never established
            pass

if __name__ == "__main__":
    create_database()
