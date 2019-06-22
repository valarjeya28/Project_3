
drop database company_db;

create database company_db;
use company_db;

create table company (
ticker varchar(6),
calendardate date,
assetturnover decimal(4,2),
currentratio decimal(4,2),
de decimal(10,2),
epsusd decimal(4,2),
grossmargin decimal(4,3),
netmargin decimal(4,3),
pe decimal(10,1),
price decimal(7,2)
);
select * from company limit 5;
create table ticker (
ticker varchar(6) primary key,
name varchar(99),
category varchar(99),
sicsector varchar(99),
currency varchar(10),
location varchar(50),
sector varchar(50)
);


select * from company limit 5;
select * from ticker limit 5;

select * from company where calendardate = "2018-12-31"
AND ticker in("XOM", "V", "UTX","GE","WMT","NKE","KO","IBM","DIS","DD");

select * from company;

select * from company a
join ticker b
on a.ticker=b.ticker
where sicsector = "Manufacturing"
AND a.ticker <> "CSCO"
and a.ticker <> "NKE"
and a.ticker <> "BA"
AND calendardate = "2018-12-31";

select distinct ticker from ticker;