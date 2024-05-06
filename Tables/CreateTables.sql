drop table if exists laptops cascade;

Create table laptops(
	laptopID int primary key,
	companyName text not null,
	typeName text not null,
	inches real not null,
	screenResolution varchar(75) not null,
	cpu varchar(50) not null,
	ram varchar(5) not null,
	memory varchar(50) not null,
	gpu varchar(100) not null,
	os varchar(30) not null,
	laptopWeight varchar(30) not null,
	priceInUSDollars real not null
);

\copy laptops from 'laptop_data_WithUSPrices.csv' DELIMITER ',' CSV
