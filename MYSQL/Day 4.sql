create database tcl;
use tcl;
create table orders(
order_id int primary key,
customer_name varchar(100),
status varchar(50)
);
desc orders;
set autocommit=0;
BEGIN;
insert into orders values(101,"RAM","Approved"),(102,"Shyam","Pending");
select * from orders;
rollback;
commit;

insert into orders values(103,"Kanak","Approved"),(104,"Bob","Pending");
 
 commit;
 rollback;
 
 
insert into orders values(101,"RAM","Approved"),(102,"Shyam","Pending");
commit;
update orders set customer_name="Raj" where order_id=102;
rollback;

insert into orders values(103,"Kanak","Approved"),(104,"Bob","Pending");
savepoint sp1;
update orders set status = "Pending" where order_id = 103;
savepoint sp2;
rollback to savepoint sp1;
rollback;