import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root",passwd="your database password" ,database="mydatabase")

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers1 (name VARCHAR(255),address VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x) 
