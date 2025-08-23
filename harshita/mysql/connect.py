import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root", auth_plugin="mysql_native_password")


if mydb.is_connected():
    print("Connection stablished")