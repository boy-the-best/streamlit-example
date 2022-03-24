import mysql.connector as c

con=c.connect(host="localhost",
              user="root",
              passwd="",
              database='streamlit')

cursor=con.cursor()

script="""select * from persons"""

cursor.execute(script)


a=cursor.fetchall()
for i in a:
    print(i)
