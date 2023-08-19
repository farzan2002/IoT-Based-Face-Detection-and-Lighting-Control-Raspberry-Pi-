import mysql.connector





def mysqlsearch(name):
       mydb = mysql.connector.connect(
       host= "localhost",
       user="root",
       password="",
       database="attendance"

)

       a = mydb.cursor()
       sql1=a.execute("SELECT * from Students WHERE Student_NAME = %(name)s", {'name': name})

       a.execute(sql1)
       checkUsername = a.fetchall()
       print(*checkUsername, sep = "\n")

       mydb.commit()
       mydb.close()

name=input("Enter Student_Name:-")
mysqlsearch(name)
        
         
         
         
         
        
