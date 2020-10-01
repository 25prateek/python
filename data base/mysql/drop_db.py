import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root",passwd="Mysql12345!@#$%")

mycursor = mydb.cursor()
sql = "DROP DATABASE mydatabas"

mycursor.execute(sql) 
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
