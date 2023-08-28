import pytest
import infrastructure
import modules.books
import modules.loans
import modules.customers
import  pyodbc

#infrastructure.execute(
'''
create table BooksTests
(Id int primary key identity (1,1)
,Name varchar (100) not null
,Author varchar (100) not null
,YearPublished int not null
,Type int not null'''



#infrastructure.cursor.execute("insert into	Bookstests values ( 'testbook1', 'testauthor1' , 1111 , 1)")
#infrastructure.conn.commit()
'''
i = infrastructure.SqlInteraction()
i.table = "bookstests"
b = modules.books.Books()
b.table = "bookstests"

def test_printTable(capsys):
    i.printTable()
    captured = capsys.readouterr()
    assert captured.out == "(1, 'testbook1', 'testauthor1', 1111, 1)\n\n\n"

#b.addBook ('testbook2', 'testauthor2', 2222, 2)

def test_addBook(capsys):
    b.printTable()
    captured = capsys.readouterr()
    assert captured.out == ("(1, 'testbook1', 'testauthor1', 1111, 1)\n"
 '\n'
 '\n'
 "(2, 'testbook2', 'testauthor2', 2222, 2)\n"
 '\n'
 '\n')



'''

def test_addBook():
    pass
#everything works as expected, run main for  detailed tests
#settig up fixtures and mockers and so on is yet to be figured out.....
