import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root",passwd="your_password")

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabae")


mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
