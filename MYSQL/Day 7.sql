-- Joins

create database basicjoin;
use basicjoin;
create table employees(
employee_id int primary key,
ename  varchar(50)
);
insert into employees values(101,"Raju"),(102,"Rishabh"),(103,"Mohan"),(104,"Rohan"),(105,"Sanjay");

select * from employees;

create table projects(
project_id int primary key,
pname varchar(50),
employee_id int,
foreign key(employee_id) references employees(employee_id)
);
desc projects;

insert into projects values(1,"Project A",101),(2,"Project B",102),(3,"Project C",101),(4,"Project D",103),(5,"Project E",103),(6,"Project F",Null);


select * from employees join projects on employees.employee_id = projects.employee_id;

select e.ename,p.pname from projects p inner join employees e on e.employee_id = p.employee_id;

select e.employee_id,e.ename,p.pname from employees e left join projects p on e.employee_id=p.employee_id;

select e.employee_id,e.ename,p.pname from projects p left join employees e on e.employee_id=p.employee_id;

