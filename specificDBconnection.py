import mysql.connector as connector


def specific_db_connection():
    mydb = connector.connect(
        host='',
        user='',  # username of your database
        password='',  # password of your database
        database=''   # name of your database
    )

    if mydb:
        print("pyDatabase is connected successfully")
