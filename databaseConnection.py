import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="HOSTNAME",
            port='PORT',
            user="USERNAME",
            password="PASSWORD",
            database="DATABASE_NAME"
        )
        print("Connected to the database successfully")
        return connection
    except mysql.connector.Error as e:
        raise e
