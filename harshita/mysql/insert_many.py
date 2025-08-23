import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="library", auth_plugin="mysql_native_password")


cursor = mydb.cursor()

insertion = 'INSERT INTO books(book_id, title, price) VALUES(%s, %s, %s)'

data = [
    (103, "Thor", 34.50),
    (104, "Iron man", 51.25),
    (105, "Captain America", 15.00)
]

cursor.executemany(insertion, data)

mydb.commit()