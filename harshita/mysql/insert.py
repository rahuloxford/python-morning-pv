import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="library", auth_plugin="mysql_native_password")


cursor = mydb.cursor()

insertion = 'INSERT INTO books(book_id, title, price) VALUES(%s, %s, %s)'

data = (102, "Spider man", 25.33)

cursor.execute(insertion, data)

mydb.commit()