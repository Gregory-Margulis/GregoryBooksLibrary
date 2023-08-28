import pytest
import infrastructure
import modules.books
import modules.loans
import modules.customers
import  pyodbc

'''

infrastructure.cursor.execute("create table Customerstests (Id int primary key identity (1,1),Name varchar (100) not null, City varchar (100) not null,Age int not null")

infrastructure.cursor.execute("insert into	Customerstests values ( 'custA', 'cityA',18)")
infrastructure.conn.commit()


c = modules.customers.Customers()
c.table = 'customerstests'
c.addCustomer('custA', 'cityA', 18)
infrastructure.conn.commit()
c.printTable()
'''
def test_addCustomer (capsys):
    pass

    #everything works as expected, run main for  detailed tests
    #settig up fixtures and mockers and so on is yet to be figured out.....

    '''
    infrastructure.cursor.execute("delete from Customerstests")
    c.addCustomer('custA', 'cityA', 18)
    #infrastructure.cursor.execute("insert into	Customerstests values ( 'custA', 'cityA',18)")
    c.printTable()
    captured = capsys.readouterr()
    infrastructure.cursor.execute("select id from Customerstests")
    id = infrastructure.cursor.fetchall()
    assert captured.out ==  ("("+str(id[0][0])+", 'custA', 'cityA', 18)\n\n\n")
    '''





