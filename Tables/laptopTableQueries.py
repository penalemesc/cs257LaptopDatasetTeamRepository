import psycopg2

# This function gets the laptops that cost over 3000.
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

    row = cur.fetchall()

    return str(row)

print(laptopsOverThreeThousand())
