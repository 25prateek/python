import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root",passwd="Mysql12345!@#$%" ,database="mydatabase")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE name_t (name VARCHAR(255),address VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x) 
