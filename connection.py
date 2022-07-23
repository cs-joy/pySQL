import mysql.connector as connector


def connection():
    mydb = connector.connect(
        host='',
        user='',  # username of your database
        password=''  # password of your database
    )

    if mydb:
        print("Successfully Connected!")
