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

    max_finder = "SELECT companyName, typeName FROM laptops WHERE priceInUSDollars = (SELECT MAX(priceInUSDollars) FROM laptops);"

    cur.execute(max_finder)

    row = cur.fetchall()

    return row

print(maxPrice())