drop table if exists laptops cascade;
drop table if exists lPrice cascade;

Create table laptops(
	lID int primary key,
	companyName varchar(30) not null,
	typeName varchar(30) not null,
	inches real not null,
	screenResolution varchar(75) not null,
	cpu varchar(50) not null,
	ram varchar(5) not null,
	memory varchar(50) not null,
	gpu varchar(100) not null,
	os varchar(30) not null,
	lWeight varchar(30) not null
);

Create table lPrice(
	lID int primary key REFERENCES laptops (lID),
	priceInRupees real not null,
	conversion real not null,
	priceInUSDollars real not null
);

\copy laptops from 'laptopDataWithNoMoney.csv' DELIMITER ',' CSV
\copy lPrice from 'laptopPrices.csv' DELIMITER ',' CSV