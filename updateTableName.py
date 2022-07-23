import mysql.connector as connector


def update_table_name():
    mydb = connector.connect(
        host='',
        user='',  # username of your database
        password='',  # password of your database
        database=''   # name of your database
    )

    if mydb:
        cursor = mydb.cursor()
        if cursor:
            cursor.execute("ALTER TABLE cars RENAME TO cats")
