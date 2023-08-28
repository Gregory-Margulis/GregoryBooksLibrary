import infrastructure
from datetime import date


'''
by: Gregory Margulis
dsate: 14/08/2023
description: defines book loaning methods and variables
'''

class Loans (infrastructure.SqlInteraction):
    def __init__(self):
        #super().__init__()
        self.table = "Loans"

    def loanBook(self, custId, bookId, loanDate):
        '''
            author: Gregory
            Date: 26/08/23
            args: values of loan (without return  date)
            action: inserts values to the loans table
        '''
        self.custId = custId
        self.bookId = bookId
        self.loadDate = loanDate
        # toAddLater: try and catch (for nonexistent books / customers)
        # toAddLater: error message for unreasonable loan date
        # toAddLater: error message for books that are currently not available (laoned)
        self.defaultReturnDate = '9999-12-31'

        infrastructure.cursor.execute('insert into	loans values ( ?, ? , ? , ?)', self.custId, self.bookId, self.loadDate, self.defaultReturnDate)
        infrastructure.conn.commit()

        print ("loan added")


    def returnBook(self,custId,bookId,loanDate,returnDate):

        '''
            author: Gregory
            Date: 26/08/23
            args: values of loan and a return  date
            action: updates the return date
        '''
        self.returnDate = returnDate
        self.custId = custId
        self.bookId = bookId
        self.loadDate = loanDate
        # toAddLater: try and catch (for nonexistent loans)
        # toAddLater: error message for unreasonable return date
        # all 3 params custID, BookID and loanDate must be transferred to where condition to avoid updating the wrong loan
        infrastructure.cursor.execute('update loans set returndate = ? where  custId = ? and bookId =  ? and loanDate = ? ', self.returnDate, self.custId, self.bookId, self.loadDate)
        infrastructure.conn.commit()
        print ("loan returned")

    def lateLoans(self):
        '''
            author: Gregory
            Date: 26/08/23
            return: all late loans (returned and unreturned).
            late loans are defined by the type of the book:
            1 – up to 10 days
	        2 – up to 5 days
	        3 – up to 2 days
        '''


        self.today = date.today()
        infrastructure.cursor.execute ('''select * from loans inner join books on loans.BookId = books.id where 
        (DATEDIFF(day, loans.loandate, loans.returndate) > 2) and loans.returndate != ?  and books.type = 3
        or DATEDIFF (day, loans.loandate, loans.returndate) > 5 and loans.returndate != ? and books.type = 2
        or DATEDIFF (day, loans.loandate, loans.returndate) > 10 and loans.returndate != ?  and books.type = 1
        or loans.returndate =  ? and DATEDIFF(day, loans.loandate, ? ) > 2 and books.type = 3 
        or loans.returndate = ? and DATEDIFF(day, loans.loandate, ? ) > 5 and books.type = 2 
        or loans.returndate = ? and DATEDIFF(day, loans.loandate, ? ) > 10 and books.type = 1''', str(self.defaultReturnDate), str(self.defaultReturnDate), str(self.defaultReturnDate), str(self.defaultReturnDate), str(self.today), str(self.defaultReturnDate), str(self.today), str(self.defaultReturnDate), str(self.today))
        print ('late loans:')
        self.result = infrastructure.cursor.fetchall()
        for row in self.result:
            print(row)
            print("\n")

        infrastructure.conn.commit()
