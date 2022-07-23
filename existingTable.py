import mysql.connector as connector


def existing_table():
    mydb = connector.connect(
        host='',
        user='',  # username of your database
        password='',  # password of your database
        database=''   # name of your database
    )

    if mydb:
        cursor = mydb.cursor()

        if cursor:
            cursor.execute("ALTER TABLE blogs ADD COLUMN lastUpdate DATETIME")
