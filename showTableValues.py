import mysql.connector as connector


def show_table_values():
    mydb = connector.connect(
        host='',
        user='',  # username of your database
        password='',  # password of your database
        database=''   # name of your database
    )

    if mydb:
        cursor = mydb.cursor()
        if cursor:
            cursor.execute("show fields from blogs")
            for tableValues in cursor:
                print(tableValues)

