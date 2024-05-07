# MaxPrice_Laptop.py
# Authors: THe Blind Ones

# This following program was designed in order to return
# the laptop with the highest price.

import psycopg2


def laptopsWithTouchScreen():

    # Establishing Environment
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm")

    cur = conn.cursor()

    searchTouchScreen = "SELECT Laptop_Name, Price, Touchscreen FROM laptops WHERE Touchscreen = TRUE FROM laptops);"

    cur.execute(searchTouchScreen)
    row = cur.fetchall()
    
    return "Here are all the laptops with a TouchScreen: " + row

laptopsWithTouchScreen()