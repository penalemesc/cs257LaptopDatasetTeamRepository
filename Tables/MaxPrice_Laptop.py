# MaxPrice_Laptop.py
# Authors: THe Blind Ones

# This following program was designed in order to return
# the laptop with the highest price.

import psycopg2


def maxPrice():

    # Establishing Environment
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm")

    cur = conn.cursor()

    max_finder = "SELECT Brand, Laptop_Name, Price FROM laptops WHERE Price = (SELECT MAX(Price) FROM laptops);"

    cur.execute(max_finder)
    row = cur.fetchall()[0]

    comp_row = row[0]
    type_row = row[1]
    price_row = row[2]

    print("The most expensive laptop is a " + str(comp_row) + " " +  str(type_row) + " laptop.")
    print("It costs $" + str(price_row) + "!")

maxPrice()