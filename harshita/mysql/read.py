import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="library", auth_plugin="mysql_native_password")


cursor = mydb.cursor()

read_query = "SELECT * FROM books"

cursor.execute(read_query)

# result = cursor.fetchone()
# result = cursor.fetchmany(3)
result = cursor.fetchall()

for res in result:
    print(res)