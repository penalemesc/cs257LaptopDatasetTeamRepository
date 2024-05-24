# LaptopsByBrand.py
# Authors: THe Blind Ones

# This program is designed to return all the laptops of a specific brand given by the user.

import psycopg2

def laptopsByBrand():
    # Establishing Environment
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm")
    
    cur = conn.cursor()

    brand = input("Please enter the laptop brand you're interested in: ").lower()

    query = "SELECT laptop_name, price FROM laptops WHERE brand = %s;"
    cur.execute(query, (brand,))

    rows = cur.fetchall()

    # Check if any laptops were found
    if rows:
        print(f"Laptops found for brand {brand}:")
        for row in rows:
            print(f"{row[0]} - ${row[1]}")
    else:
        print(f"No laptops found for brand {brand}.")

    cur.close()
    conn.close()

laptopsByBrand()
