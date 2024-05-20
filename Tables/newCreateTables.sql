DROP TABLE IF EXISTS laptops cascade;

    CREATE TABLE laptops (
    laptopIndex int NOT NULL PRIMARY KEY,
    Brand text not null,
    Laptop_Name varchar(150) not null,
    Price real not null,
    Processor_Brand text not null,
    CPU varchar(30) not null,
    RAM int not null,
    Storage_Type text not null,
    Storage int not null,
    GPU varchar(15) not null,
    GPU_Type text not null,
    Touchscreen text not null,
    Screen_Size real not null,
    OS text not null
    );

\copy laptops from 'newLaptopData.csv' DELIMITER ',' CSV
