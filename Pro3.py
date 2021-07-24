import mysql.connector as mysql

# Connection Object Prepare
cnn = mysql.connect(host="localhost",database="pydb",user="root",password="")

# Cursor Object : for execute SQL Queries
cr = cnn.cursor()

cr.execute("select * from student")

while True:
    rec = cr.fetchmany(2)
    if len(rec)==0:
        break
    print("\n",rec)

cnn.close()


