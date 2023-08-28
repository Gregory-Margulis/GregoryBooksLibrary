import pytest
import infrastructure
import modules.books
import modules.loans
import modules.customers
import  pyodbc
l = modules.loans.Loans()
'''
infrastructure.cursor.execute("""
create table Loanstests
(CustId int foreign key references Customers (Id)
,BookId int foreign key references Books (Id)
,LoanDate date not null
,returnDate date)
""")
'''
"""
def test_lateLoans
(1, 1, datetime.date(2023, 8, 14), datetime.date(9999, 12, 31), 1, 'ayelet metayelet', 'pushkin', 1547, 2)


(1, 15, datetime.date(2023, 8, 27), datetime.date(2023, 8, 30), 15, 'shmulikipod', 'dvora omer', 1854, 3)


(1, 17, datetime.date(2023, 8, 27), datetime.date(9999, 12, 31), 17, 'shmulikipod', 'dvora omer', 1854, 3)
"""

'''
@pytest.fixture
def getLoansTestTable ():
    pass
'''
def test_loan():
    pass

#everything works as expected, run main for  detailed tests
#settig up fixtures and mockers and so on is yet to be figured out.....
