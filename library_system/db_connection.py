# db_connection.py
import mysql.connector
from mysql.connector import Error
from config import db_config

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._init_connection()
        return cls._instance

    def _init_connection(self):
        try:
            self.conn = mysql.connector.connect(**db_config)
            if self.conn.is_connected():
                print("Successfully connected to the MySQL database")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.conn = None

    def get_connection(self):
        return self.conn

    def close_connection(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("MySQL connection closed.")
            DatabaseConnection._instance = None
