create database organization;
use organization;
create table employee(
empid int not null primary key,
first_name varchar(15),
last_name varchar(15),
gender char,
role varchar(15),
dept varchar(15),
manager_id varchar(10)
);

insert into employee values(1,"Raj","Sharma","M","Developer","IT","10#1"),
(2,"Raunak","Verma","M","HR","IT","10#2"),
(3,"Suhani","karma","F","Admin","Sales","10#3"),
(4,"Girish","Bal","M","Consultant","Marketing","10#4"),
(5,"Meghna","Bali","F","Support","IT","10#5");

select distinct(dept) from employee order by dept;
select distinct(role) from employee order by role;

select * from employee where role="HR" and dept="IT";
select * from employee where role="HR" and dept="Sales";

select * from employee where role="HR" or dept="Sales";

select * from employee where role in ("HR","Admin");
select * from employee where role not in ("HR","Admin");

alter table employee add column experience int;

update employee set experience = 1 where empid = 1;
update employee set experience = 3 where empid = 3;
update employee set experience = 5 where empid = 5;

select * from employee where experience between 3 and 10;
select * from employee where experience = 2 or experience = 10;

select * from employee where last_name like "S%";

select * from employee order by experience limit 5;

select * from employee where experience is null;

select count(empid) from employee where dept = "Finance";
select min(empid) from employee;
select max(empid) from employee;
select sum(experience) from employee;
select count(*) from employee;
select count(empid) from employee where role = "Developer";
select avg(experience) from employee;

select dept,count(*) from employee group by dept;
select role,count(*) from employee group by role;

select dept,count(*) from employee group by dept having dept = "IT";
select dept,sum(experience) from employee group by dept having sum(experience)>=1 and sum(experience)<=5 and dept = "IT";
select * from employee;

select dept,count(empid) from employee group by dept having count(empid)>2 order by count(empid) desc;

