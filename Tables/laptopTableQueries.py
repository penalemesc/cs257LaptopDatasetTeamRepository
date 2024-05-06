import psycopg2

# This function gets the laptops that cost over 1000.
def laptopsOverOneThousand():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm")

    cur = conn.cursor()

    sql = "SELECT * FROM laptops WHERE priceInUSDollars > 1000"

    cur.execute(sql)

    row = cur.fetchall()

    return row

print(laptopsOverOneThousand())