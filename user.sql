create database SSE;

use SSE;


create table user(
        name varchar(50),
        email varchar(80),
        userID int,
        pw varchar(130)
);

# drop table user; # delete table

show tables; 


insert into user(name, email, userID, pw) values
("autekwing", "autekwing@ucla.edu", 1, "e10adc3949ba59abbe56e057f20f883e");

insert into user(name, email, userID, pw) values
("autekwing", "autekwing@ucla.edu", 2, "c33367701511b4f6020ec61ded352059");

select * from SSE.user; # see all data in table

select * from SSE.user where userID=1; 
select name from SSE.user where userID=1;
