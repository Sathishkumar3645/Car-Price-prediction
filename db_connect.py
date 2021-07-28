from flask import Flask, render_template, request
import jsonify
import requests
from tabulate import tabulate
import mysql.connector


app = Flask(__name__)

mydb = mysql.connector.connect(
        host        =   "localhost",
        user        =   "root",
        password    =   "Sathish=3645",
        database    =   "cars"
    )
    
mycursor = mydb.cursor()

@app.route("/", methods =   ['POST','GET'])
def dashboard():
    return render_template('loginpage.html')

@app.route("/register", methods = ["POST","GET"])
def signup():
 
  if request.method =='POST':
    f_name      =   request.form['name']
    f_userid    =   request.form['userid']
    f_password  =   request.form['password']
    f_emailid   =   request.form['emailid']
    f_number    =   request.form['number']
    f_amount    =   request.form['amount']
   

    sql = "INSERT INTO login (name , userid , emailid , password , phonenumber , amount ) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (f_name , f_userid , f_emailid , f_password , f_number , f_amount)
    mycursor.execute(sql, val)
    mydb.commit()

    return render_template("loginpage.html") 

@app.route("/allow", methods = ["POST","GET"])
def login():

    if request.method == "POST":
        f_userid    =   request.form['userid']
        f_password  =   request.form['password']
        print(f_userid)

        sql = "SELECT * FROM login WHERE userid = %s "
       
        val = (f_userid , )
        mycursor.execute(sql , val)
        result = mycursor.fetchall()

        for x in result:
            d_username = x[1]
            d_password = x[3]
            print("hi")
            print(d_username)
            if d_username == f_userid :
                print("Login Successfull")
                return render_template("new.html") 

    print("Incorrect Username")
    return render_template("loginpage.html") 
            

if __name__=="__main__":
    app.run(debug=True)