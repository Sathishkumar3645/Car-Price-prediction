<br><br><h3>{{ price_text }}</h3>


def temp_val(num):
     
    # connect python with mysql with your hostname,
    # username, password and database
    db = MySQLdb.connect("localhost", "root", "Sathish=3645", "cars")
      
    # get cursor object
    cursor = db.cursor()
      
    # execute your query
    cursor.execute("SELECT * FROM newcars")
      
    # fetch all the matching rows
    result = cursor.fetchall()
      
    # loop through the rows
    for row in result:
        print(row, '\n')
        
        
        temp = temp_val(num)
        
        
        
        if string<0:
        return render_template('index1.html',price_text="Sorry!!! No cars available at this price ")
    else:
        return render_template('index1.html', price_text= "Available cars are {}".format(list(temp)))