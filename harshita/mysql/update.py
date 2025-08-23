import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="library", auth_plugin="mysql_native_password")


cursor = mydb.cursor()

update_query = "UPDATE books SET price = price + 10 WHERE price > 20"

cursor.execute(update_query)


mydb.commit()