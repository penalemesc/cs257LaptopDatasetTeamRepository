import psycopg2

# This function gets the laptops that cost over 1000.
def laptopsOverThreeThousand():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm")

    cur = conn.cursor()

    sql = "SELECT Laptop_Name FROM laptops WHERE Price > 3000"

    cur.execute(sql)

    row = cur.fetchall()[0]

    laptopName = row[2]

    return laptopName

print(laptopsOverThreeThousand())
