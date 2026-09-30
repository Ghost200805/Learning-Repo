create database CompanyDB;
use CompanyDB;
create table Employees(
EmpId int primary key,
EmpName varchar(30),
Salary int(10),
JoinDate date);

create table Departments(
DeptID int primary key,
DeptName varchar(30));

alter table employees add column Email varchar(100);

alter table departments add column dept_location varchar(100);

alter table employees add Phoneno int(10);
alter table employees modify Phoneno int(10) not null;


alter table employees modify EmpName varchar(100);

alter table employees add constraint foreign key(EmpID) references departments(DeptID);
alter table departments add constraint foreign key(DeptID) references employees(EmpID);

alter table departments drop foreign key departments_ibfk_1;
alter table employeedetails drop foreign key employeedetails_ibfk_1;

alter table employees rename column EmpName to EmployeeName;

alter table employees drop column Phoneno;

alter table employees rename EmployeeDetails;

desc departments;
desc employees;

drop table departments;
drop table employees;
drop table employeedetails;

show create table departments;
show create table employees;

show tables;

drop database companydb;