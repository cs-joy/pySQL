import mysql.connector as connector


def create_table():
    mydb = connector.connect(
        host='',
        user='',  # username of your database
        password='',  # password of your database
        database=''   # name of your database
    )

    if mydb:
        cursor = mydb.cursor()
        if cursor:
            print("create table successfully!")
            cursor.execute("CREATE TABLE cars (name VARCHAR(255), gender VARCHAR(255))")

