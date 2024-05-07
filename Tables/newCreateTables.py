import psycopg2

# Connect to database
conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm"
        )

# Open cursor to perform database operations
cur = conn.cursor()

# Create new tables

laptopTable = """DROP TABLE IF EXISTS laptops cascade;

            CREATE TABLE laptops (
            Laptop_Name varchar(150) not null,
            Brand text not null,
            Model varchar(15) not null,
            CPU varchar(30) not null,
            RAM int not null,
            Storage int not null,
            Storage_Type text not null,
            GPU varchar(15) not null,
            Screen_Size real not null,
            Touchscreen text not null,
            Price real not null
            );
            """

copyLaptopData = "copy laptops from 'laptopData.csv' DELIMITER ',' CSV"

cur.execute(laptopTable)
cur.execute(copyLaptopData)

conn.commit()
