create database user;
use user;
create table customer(
custid int, 
custname varchar(15),
city varchar(10),
product varchar(15),
price int
);

desc customer;

alter table customer add primary key(custid);
insert into customer values(1,"Om","Pune","Mobile",15000);
insert into customer values(2,"Rucha","Nagpur","Laptop",40000);
insert into customer values(3,"Raj","Mumbai","Mouse",300);

select * from customer;

select custname,product from customer;

create table clonetable as select * from customer;
select * from clonetable;
drop table clonetable;

select custname,city from customer;
select custname, city from customer where custid = 1;
select custname,product,price from customer where price>15000;
select * from customer where price>=15000;
select * from customer where custid=1;
select * from customer where city = "nagpur";
select * from customer order by price;
select * from customer order by price desc;
select * from customer order by custid desc;
select * from customer order by city desc , price asc;

select upper(custname), lower(product) from customer where custid<3;

alter table customer add lastname varchar(30);

update customer set lastname = "Sharma" where custid = 1;
update customer set lastname = "Verma" where custid = 2;
update customer set lastname = "Kumar" where custid = 3;

select concat(custname," ",lastname) from customer;
select concat(custname," ",lastname) as Fullname from customer;

select substr(custname,1,3) from customer;

select instr(custname,"a") from customer;

select * from customer;
select substr(custname,1,3), instr(custname,'a') from customer;

select now() as curr_time;

alter table customer add column date date;

update customer set date='2024/2/20' where custid = 1;
update customer set date='2024-8-24' where custid = 2;
update customer set date='2024-10-21' where custid = 3; 

alter table customer drop column date;