-- create database imcc;
-- use imcc;
-- create table students (student_id int, name varchar(50), age int, course varchar(50));

-- insert into students values(5,"MNO",21,null);

-- set SQL_SAFE_UPDATES = 0;

-- update students set age = 23 where student_id = 1;

-- delete from students where student_id = 1;

select name,age from students where student_id>3;