drop table if exists laptops cascade;
drop table if exists laptopPrices cascade;

Create table laptops(
	laptopID int primary key,
	companyName varchar(30) not null,
	typeName varchar(30) not null,
	inches real not null,
	screenResolution varchar(75) not null,
	cpu varchar(50) not null,
	ram varchar(5) not null,
	memory varchar(50) not null,
	gpu varchar(100) not null,
	os varchar(30) not null,
	laptopWeight varchar(30) not null
);

Create table laptopPrice(
	laptopID int primary key REFERENCES laptops (laptopID),
	priceInUSDollars real not null
);

\copy laptops from 'laptopDataWithNoMoney.csv' DELIMITER ',' CSV
\copy laptopPrices from 'laptopPrices.csv' DELIMITER ',' CSV