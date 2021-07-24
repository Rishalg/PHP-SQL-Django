import mysql.connector as mysql

# Connection Object Prepare
cnn = mysql.connect(host="localhost",database="pydb",user="root",password="")

# Cursor Object : for execute SQL Queries
cr = cnn.cursor()

cr.execute("select * from student")

data = cr.fetchall()
print(data)

cnn.close()


