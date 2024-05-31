from flask import Flask, render_template, jsonify
import psycopg2
import json

app = Flask(__name__)

#Welcome Page
@app.route('/')
def welcome():
    return render_template("mainWebsite.html")

@app.route('/about-us')
def aboutUsPage():
    return render_template("aboutUs.html")

#Displays the filtered options results
@app.route('/display/<brand>/<ram>/<storage>/<screenSize>/<touchScreen>/<priceRange>')
def displayLaptopChosen(brand, ram, storage, screenSize, touchScreen,priceRange):
    return render_template("filterOutput.html")

#Gathers the result for filtered options and return the JSON data
@app.route('/json/<brand>/<ram>/<storage>/<screenSize>/<touchScreen>/<priceRange>')
def laptopBrandChosen(brand, ram, storage, screenSize, touchScreen,priceRange):
    # Establishing Environment
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="arizavarar",
        user="arizavarar",
        password="expo795beach"
    )
    
    cur = conn.cursor()
    if ram != "null":
        intRam = int(ram)
    
    if storage != "null":
        intStor = int(storage)

    if screenSize != "null":
        screenSizeLowerBound = float(screenSize.split("_")[0])
        screenSizeUpperBound = float(screenSize.split("_")[1])
    
    if priceRange != "null":
        minPrice = float(priceRange.split("_")[0])
        maxPrice = float(priceRange.split("_")[1])
      

    query = '''
            SELECT Laptop_Name, Price, CPU, RAM, 
            Screen_Size, Touchscreen, laptopindex, Storage FROM laptops 
            WHERE 
            '''
    
    listVars = []

    if brand != "null":
        if len(listVars) != 0:
            query += " AND "
        query += " Brand = %s "
        listVars.append(brand)
    
    if ram != "null":
        if len(listVars) != 0:
            query += " AND "
        query += " RAM = %s"
        listVars.append(ram)

    if storage != "null":
        if len(listVars) != 0:
            query += " AND "
        query += " Storage = %s"
        listVars.append(storage)

    if screenSize != "null":
        if len(listVars) != 0:
            query += " AND "
        query += " Screen_Size >= %s" + " AND Screen_Size < %s"
        listVars.append(screenSizeLowerBound)
        listVars.append(screenSizeUpperBound)

    if touchScreen != "null":
        if len(listVars) != 0:
            query += " AND "
        query += " Touchscreen = %s"
        listVars.append(touchScreen)
    
    if priceRange != "null":
        if len(listVars) != 0:
            query += " AND "
        query += " Price >= %s" + " AND Price <= %s"
        listVars.append(minPrice)
        listVars.append(maxPrice)


    cur.execute(query, listVars)
    print(query, listVars)

    rows = cur.fetchall()

    
    #this checks so that if there are no any laptops that match the specification, the site doesnt crash
    if not rows:
        cur.close()
        conn.close()
        return jsonify(message="No laptops Matched Your Specifications")
    
    laptopsName = [row[0] for row in rows]
    laptopsPrices = [row[1] for row in rows]
    laptop_CPU = [row[2] for row in rows]
    laptop_RAM = [row[3] for row in rows]
    laptop_screensize =  [row[4] for row in rows]
    laptop_touchscreen =  [row[5] for row in rows]
    laptopImages = [row[6] for row in rows]
    laptopStorage = [row[7] for row in rows]
    
    
    cur.close()
    conn.close()
    
    json_answer = {'nameForLaptop' : laptopsName, 
                   'priceForLaptop' : laptopsPrices,
                   'CpuForLaptop' : laptop_CPU, 
                   'RamForLaptop' : laptop_RAM,
                   'screensizeLaptop' : laptop_screensize, 
                   'touchscreenLaptop' : laptop_touchscreen, 
                   'imageIndex': laptopImages,
                   'storageForLaptop':laptopStorage}
                   
    return json.dumps(json_answer)

#This is meant to be displayed if there is nothing written in the search bar
@app.route('/display/')
def nothingToDisplay():
    return render_template("errorSearchOutput.html")

#Displays the search result page
@app.route('/display/<wordSearched>')
def displaySearched(wordSearched):
    return render_template("searchOutput.html")

#Gather the searched word content and returns JSON data
@app.route('/search/<wordSearched>')
def searchFunction(wordSearched):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="arizavarar",
        user="arizavarar",
        password="expo795beach"
    )
    
    cur = conn.cursor()

    query = '''
            SELECT Laptop_Name, Price, CPU, RAM, 
            Screen_Size, Touchscreen, laptopindex, Storage FROM laptops WHERE 
            Brand iLIKE %s OR 
            Laptop_Name iLIKE %s OR 
            CAST(Price AS TEXT) iLIKE %s OR 
            Processor_Brand iLIKE %s OR 
            GPU iLIKE %s OR 
            OS iLIKE %s;
            '''
    
    search_pattern = '%' + wordSearched + '%'
    cur.execute(query, (search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern))

    rows = cur.fetchall()

    #this checks so that if there are no any laptops that match the specification, the site doesnt crash
    if not rows:
        cur.close()
        conn.close()
        return jsonify(message="No laptops Matched Your Specifications")

    laptopsName = [row[0] for row in rows]
    laptopsPrices = [row[1] for row in rows]
    laptop_CPU = [row[2] for row in rows]
    laptop_RAM = [row[3] for row in rows]
    laptop_screensize =  [row[4] for row in rows]
    laptop_touchscreen =  [row[5] for row in rows]
    laptopImages = [row[6] for row in rows]
    laptopStorage = [row[7] for row in rows]
    
    
    cur.close()
    conn.close()

    json_answer = {'nameForLaptop' : laptopsName, 
                   'priceForLaptop' : laptopsPrices,
                   'CpuForLaptop' : laptop_CPU, 
                   'RamForLaptop' : laptop_RAM,
                   'screensizeLaptop' : laptop_screensize, 
                   'touchscreenLaptop' : laptop_touchscreen, 
                   'imageIndex': laptopImages,
                   'storageForLaptop':laptopStorage}
    
    return json.dumps(json_answer)

if __name__ == '__main__':
    my_port = 5120
    app.run(host='0.0.0.0', port=my_port)

