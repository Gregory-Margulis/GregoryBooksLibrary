use master
create database GregoryBooksLibrary

use GregoryBooksLibrary
create table Books
(Id int primary key identity (1,1) 
,Name varchar (100) not null
,Author varchar (100) not null
,YearPublished int not null
,Type int not null
)


insert into	Books values ('ayelet metayelet', 'rh', 2013,2)
insert into	Books values ('zahal haraev', 'ek', 1969,1	)
insert into	Books values ('hobbit', 'jrrt', 1937,3)
insert into	Books values ('harry potter', 'jkr', 1997,3)
insert into	Books values ('the witcher', 'as', 1992,2)

select * from Books

/*insert into	Bookstests values('testbook2', 'testauthor2', 2222, 2)*/

create table Customers
(Id int primary key identity (1,1) 
,Name varchar (100) not null
,City varchar (100) not null
,Age int not null
)

insert into	Customers values ('babi', 'jerusalem', 54)
insert into	Customers values ('dasha', 'zihron', 12	)
select * from Customers


create table Loans
(CustId int foreign key references Customers (Id)
,BookId int foreign key references Books (Id)
,LoanDate date not null 
,returnDate date 
)


insert into	Loans values (1,1,'2023-08-14','9999-12-31')
insert into	Loans values (2,1,'2023-08-27','2023-08-28')
insert into	Loans values (2,1,'2023-07-8','2023-07-10')
insert into	Loans values (1,15,'2023-08-27','2023-08-30')
insert into	Loans values (1,17,'2023-08-27','9999-12-31')
select * from Loans



/*
create table Customerstests (Id int primary key identity (1,1),Name varchar (100) not null, City varchar (100) not null,Age int not null)

insert into	Customerstests values ( 'custA', 'cityA',18)
delete from Customerstests

select * from customerstests
*/


