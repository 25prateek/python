import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",passwd="2Mysql12345!@#$%" ,database="mydatabase")

mycursor=mydb.cursor()

mycursor.execute("SELECT * FROM customers")

result=mycursor.fetchall()
for i in result:
	print (i)
