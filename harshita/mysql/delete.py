import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="library", auth_plugin="mysql_native_password")


cursor = mydb.cursor()

delete_query = "DELETE FROM books WHERE price >= 40"

cursor.execute(delete_query)


mydb.commit()