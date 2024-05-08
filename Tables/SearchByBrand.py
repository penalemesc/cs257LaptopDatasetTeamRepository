# MaxPrice_Laptop.py
# Authors: THe Blind Ones

# This following program was designed in order to return
# all laptops by a specific brand

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

    userinput = input()
    # max_finder = "SELECT Brand, Laptop_Name, Price FROM laptops WHERE Price = (SELECT MAX(Price) FROM laptops);"
    # max_finder = "SELECT * FROM laptops WHERE brand = %s;", (userinput)
    max_finder = "SELECT laptop_name, price FROM laptops WHERE brand = %s;", (userinput)

    cur.execute(max_finder)
    row = cur.fetchall()[0]

    type_row = row[1]
    price_row = row[2]

    print("These are the available laptops by" + userinput + ".")
    print(str(row))


maxPrice()