import mysql.connector as sql
mydb= sql.connect(host='localhost',user='root',passwd='',database="python_test")

cursor=mydb.cursor()

id=input("Enter id: ")
name=input("Enter Name: ")
DOB=input("DOB: ")

query="Insert into emp values('{}','{}','{}')".format(id,name,DOB)

cursor.execute(query)
mydb.commit()
print("Data Inserted Succesfully...:")
