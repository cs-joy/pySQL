import mysql.connector as connector


def primary_key():
    mydb = connector.connect(
        host='',
        user='',  # username of your database
        password='',  # password of your database
        database=''   # name of your database
    )

    if mydb:
        cursor = mydb.cursor()
        if cursor:
            cursor.execute(
                "CREATE TABLE blogs (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), category "
                "VARCHAR(255))")

            print("successfully created `blogs` table")
