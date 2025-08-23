import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root", auth_plugin="mysql_native_password")


cursor = mydb.cursor()

cursor.execute("CREATE DATABASE library")