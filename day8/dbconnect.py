import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        connection=mysql.connector.connect(
            host="localhost",
            database="students",
            user="root",
            password="Yashu@2005"
        )
        return connection
    except Error as e:
        print(f"error connecting to mysql:{e}")
        return None