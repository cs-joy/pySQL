import mysql.connector as connector


def creation_db():
    mydb = connector.connect(
        host='',
        user='',  # username of your database
        password=''  # password of your database
    )

    if mydb:
        my_cursor = mydb.cursor()

        if my_cursor:
            print("Successfully created `pyDatabase` to your database!")
            my_cursor.execute("CREATE DATABASE pyDatabase")
