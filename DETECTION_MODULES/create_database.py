import mysql.connector

mydb = mysql.connector.connect(
       host= "localhost",
       user="root",
       password="",
     database="attendance"

)
a = mydb.cursor()
#a.execute("CREATE DATABASE source")
#a.execute("CREATE TABLE sample (Date VARCHAR(30),Student_NAME VARCHAR(255),DateTime VARCHAR(255),Roll_No VARCHAR(255), PRIMARY KEY (Date,Student_NAME))")
#sql = "DROP DATABASE source"
#a.execute(sql)
mydb.commit()
mydb.close()
