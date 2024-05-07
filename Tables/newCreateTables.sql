DROP TABLE IF EXISTS laptops cascade;

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

\copy laptops from 'laptopData.csv' DELIMITER ',' CSV
