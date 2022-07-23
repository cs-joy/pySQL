import mysql.connector as connector


def show_tables():
    mydb = connector.connect(
        host='',
        user='',  # username of your database
        password='',  # password of your database
        database=''   # name of your database
    )

    if mydb:
        cursor = mydb.cursor()
        if cursor:
            print("--Tables--")
            cursor.execute("SHOW TABLES")

            for tableName in cursor:
                print(tableName)

