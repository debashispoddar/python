
import mysql.connector
from mysql.connector import connect

con = connect(
    user ="ardit700_student",
    password ="ardit700_student",
    host ="108.167.140.122",
    database ="ardit700_pm1database"
    
    )

print("Con Type = " , type(con))
cursor = con.cursor()
cursor2 = con.cursor()
print("Cursor Type = ",type(cursor))
print(type(cursor2))

word=input("Enter the word: ")
query = cursor.execute("SELECT * from  Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()
print(results)

query2 = cursor2.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results2 = cursor2.fetchall()
print(results2)