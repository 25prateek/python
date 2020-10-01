import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",passwd="2Mysql12345!@#$%" ,database="mydatabase")

mycursor=mydb.cursor()

sql ="INSERT INTO customers (name,address) VALUES (%s,%s)"
val=("hii","masarover")

mycursor.execute(sql,val)
mydb.commit()

print(mycursor.rowcount,"record inserted")
print(mycursor.lastrowid,"id of last row")
