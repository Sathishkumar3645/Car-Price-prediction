from flask import Flask, render_template, request
import jsonify
import requests
import pickle
from tabulate import tabulate
import numpy as np
import mysql.connector
import sklearn
from sklearn.preprocessing import StandardScaler
Price = []
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))




@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


def temp_val():
    dummy = [str(i) for i in Price]
    string = float("".join(dummy))
    num = int(string)
    
    mydb = mysql.connector.connect(
        host= "localhost",
        user="root",
        password="Sathish=3645",
        database="cars"
    )
    
    mycursor = mydb.cursor()
    
    
    
    mycursor.execute("SELECT Car_Info,Showroom_Price  FROM newcars")
    rows = mycursor.fetchall()
    return render_template('index1.html', rows = rows)
    
    


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price=float(request.form['Present_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        Kms_Driven2=np.log(Kms_Driven)
        Owner=int(request.form['Owner'])
        Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        if(Fuel_Type_Petrol=='Petrol'):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        Year=2020-Year
        Seller_Type_Individual=request.form['Seller_Type_Individual']
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0	
        Transmission_Mannual=request.form['Transmission_Mannual']
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0
        prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
        output=round(prediction[0],2)
        Price.append(output)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')


@app.route("/predict1", methods=['POST'])
def predict1():
    num1 = Price
    dummy = [str(i) for i in Price]
    string = float("".join(dummy))
    num = float(string)
    
    mydb = mysql.connector.connect(
        host= "localhost",
        user="root",
        password="Sathish=3645",
        database="cars"
    )
    
    mycursor = mydb.cursor()
    
    sql = "SELECT Car_Info,Showroom_Price  FROM newcars where Showroom_Price < %s"
    
    mycursor.execute(sql,num1)
    rows = mycursor.fetchall()
    return render_template('index1.html', rows = rows)
    
        
    

if __name__=="__main__":
    app.run(debug=True)

