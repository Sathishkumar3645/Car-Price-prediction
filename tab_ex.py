import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Sathish=3645",
                database="cars"
              )

mycursor = mydb.cursor()
mycursor.execute("SELECT Car_Info,Showroom_Price  FROM newcars where Showroom_Price < 3")
myresult = mycursor.fetchall()


print(tabulate(myresult, headers=['CarName', 'Price'], tablefmt='psql'))