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

    max_finder = "SELECT companyName, typeName, priceInUSDollars FROM laptops WHERE priceInUSDollars = (SELECT MAX(priceInUSDollars) FROM laptops);"

    cur.execute(max_finder)

    comp_row = str(cur.fetchall()[0][0])
    type_row = str(cur.fetchall()[0][1])
    price_row = str(cur.fetchall()[0][2])

    print("The most expensive laptop is a " + comp_row + type_row + " laptop. It costs ",
          price_row)


print(maxPrice())