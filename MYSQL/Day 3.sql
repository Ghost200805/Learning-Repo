create database college;
use college;
create table employees(
empid int,
firstname varchar(10),
lastname varchar(10),
empage int,
empzone varchar(10));
desc employees;

insert into employees values(1,"Rita","Zade",20,"West");
insert into employees values (2,"Ram","Joshi",22,"North"),(2,Null,"Joshi",24,"North"),(3,"Ram",Null,25,Null);
insert into employees (empid,firstname,lastname) values (5,"Geeta","Rao"),(5,Null,"Garg");

select * from employees;

update employees set firstname="Sita" where empage=24;
update employees set firstname="Raunak" where lastname = "Garg";
update employees set lastname="Sita" where empage=25;
update employees set empzone="East" where empid=3;
update employees set empage="26" where firstname="geeta";
update employees set empage="26" where firstname="raunak";
update employees set lastname = "Karam" , empzone = "East" where empid = 3;
update employees set empage = 28 , empzone = "East" where firstname = "Geeta";
update employees set empzone = "South" where firstname = "Raunak";

update employees set empid = 6 where empid = 5;
update employees set empzone = "South" where empid in (1,2);

delete from employees where empage = 26;

truncate table employees;
drop table employees;
drop database college;





/* Next --------------------------------------*/






SHOW DATABASES;
CREATE DATABASE College;
USE College;
CREATE TABLE Employee(EmpID INT, FirstName VARCHAR(10) , LastName VARCHAR(10), EmpAge int , Empzone varchar(10));
DESC Employee;
INSERT INTO Employee VALUES (1, "r0ny" , "Wane", 20 , "East");
SELECT * FROM Employee;

INSERT INTO Employee VALUES (2, "John" , "Deo", 24 , "West"),
                            (3, "John" , "Wick", 19 , "North"),
                            (4, "Sam" , "Altman", 26 , "South"),
                            (5, "Sam" , null, 26 , null);

INSERT INTO Employee (EmpID , FirstName , LastName) VALUES (6, null , "Wane");
SELECT * FROM Employee;
UPDATE Employee SET LastName = "Crook" WHERE EmpID = 5;
UPDATE Employee SET EmpZone = "East" WHERE EmpID = 5;
UPDATE Employee SET EmpZone = "South" WHERE EmpID = 6;
UPDATE Employee SET EmpAge = 27,  FirstName = "Bruce" WHERE EmpID = 6;

UPDATE Employee
SET EmpAge = 29, FirstName = 'John'
WHERE EmpID IN (4, 6);

DELETE FROM Employee WHERE EmpID = 6;

TRUNCATE TABLE Employee;
DROP TABLE Employee;


DROP DATABASE CompanyDB;
CREATE DATABASE CompanyDB;
use CompanyDB;
CREATE TABLE Employee(EmpID INT NOT NULL, FirstName VARCHAR(10) , LastName VARCHAR(10), EmpAge int , Empzone varchar(10));
INSERT INTO Employee VALUES ( 1 , "Jim", "Morman", 40 , "East");
CREATE TABLE Employee1(EmpID INT NOT NULL UNIQUE, FirstName VARCHAR(10) , LastName VARCHAR(10), EmpAge int , Empzone varchar(10));
ALTER TABLE Employee1 ADD CONSTRAINT PRIMARY KEY(EmpID);
INSERT INTO Employee1 VALUES ( 2 , "Jim", "Carrie", 40 , "East");
SELECT * FROM Employee1;
CREATE TABLE Employee2(EmpID INT NOT NULL UNIQUE, FirstName VARCHAR(10) , LastName VARCHAR(10), EmpAge int , Empzone varchar(10) , CHECK(EmpAge>22));
SELECT * FROM Employee2;
INSERT INTO Employee2 VALUES ( 1 , "Jim", "Carrie", 19 , "East");
INSERT INTO Employee2 VALUES ( 1 , "Jim", "Carrie", 23 , "East");
ALTER TABLE Employee2 ADD COLUMN EmpSalary INT CHECK(EmpSalary > 5000);
INSERT INTO Employee2 VALUES ( 1 , "Jim", "Carrie", 23 , "East", 4000);
INSERT INTO Employee2 VALUES ( 2 , "Jim", "Carrie", 23 , "East", 5100);
CREATE TABLE Employee3(EmpID INT NOT NULL UNIQUE, FirstName VARCHAR(10) , LastName VARCHAR(10), EmpAge int , Empzone varchar(10) );
ALTER TABLE Employee3 ADD COLUMN EmpSalary INT;
ALTER TABLE Employee3 ADD CONSTRAINT chk_EmpAge_Salary CHECK(EmpAge >22 and EmpSalary > 5000);


create  table employee7(
empid int primary key,
firstname varchar(10),
lastname varchar(10),
empage int,
salary int);
desc employee7;
-- multiple column
alter table employee7 add constraint chk_empage_salary check (empage>20 and salary>=5000);
desc employees;
-- single column only 
alter table employees add constraint check(empage>20) ;
alter table employees add constraint chk_empage_sal check(empage>20 and empid>=1000) ;
alter table employee7 drop check chk_empage_salary;
show create table employee7;
show create table employees;

desc employee7;
alter table employee7 add constraint check(salary>=5000);

show tables;
select * from employees;

insert into employees(empid,firstname) values(10001,"Govind");
insert into employees(empid,firstname) values(10002,"Soni");
insert into employees(empid,firstname) values(10003,"Ram");
insert into employees(empid,firstname) values(10004,"Shyam");
insert into employees(empid,firstname) values(10005,"Sita");

-- delete from employees where empid=10001;
desc employees;
create index demoindex on employees(firstname);
create index deomoindex2 on employees(firstname,lastname);
show indexes from employees;

drop index demoindex on employees;
