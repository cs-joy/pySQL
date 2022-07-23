import mysql.connector as connector


def showing_db():
    mydb = connector.connect(
        host='',
        user='',  # username of your database
        password=''  # password of your database
    )

    if mydb:
        cursor = mydb.cursor()

        if cursor:
            cursor.execute("SHOW DATABASES")
            print("--Database Table--")

            for dbname in cursor:
                print(dbname)
