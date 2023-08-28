#### note: main is designed to run starting whith GregoryBooksLibrary database whith 3 empty tables (books, customers and loans)
# Gregory Margulis project1 : GregoryBooksLibrary
#submit date: 29/08/23

import infrastructure
import modules.books
import modules.loans
import modules.customers
import  pyodbc

#toAddLater: automatic code formatting

if __name__ == '__main__':

    b = modules.books.Books()
    c = modules.customers.Customers()
    l = modules.loans.Loans()
    i = infrastructure.SqlInteraction()
    #test books module:
    b.printTable()
    b.addBook('hobbit', 'jrrt', 1937, 3)
    print("____________________________________")
    b.printTable()

    bookid = b.find('hobbit')

    b.removeBook(bookid)

    b.printTable()

    b.addBook('ayelet metayelet', 'rh', 2013, 2)
    b.addBook('harry potter', 'jkr', 1997, 3)
    b.addBook('the witcher', 'as', 1992, 1)

    
    print("____________________________________")
    #test customers module:
    c.printTable()

    c.addCustomer('babi', 'jerusalem', 54)
    c.addCustomer('dasha', 'zihron', 12)
    c.addCustomer('gregory', 'meizar', 35)

    c.printTable()

    customerid = c.find('dasha')

    print("____________________________________")
    
    c.removeCustomer(customerid)
    c.printTable()
    #test loans module:
    ayeletMetayeletid = b.find('ayelet metayelet') #type3
    harryPotterid = b.find('harry potter') #type2
    witcherid = b.find('the witcher') #type1
    babiid = c.find('babi')
    gregoryid = c.find('gregory')

    print("____________________________________")

    l.loanBook(babiid, ayeletMetayeletid, '2023-08-14')
    l.loanBook(gregoryid, harryPotterid, '2023-08-27')
    l.loanBook(babiid, witcherid, '2022-04-14')
    l.loanBook(gregoryid, harryPotterid,'2023-06-22')
    l.loanBook(gregoryid, ayeletMetayeletid, '2023-03-21')
    l.loanBook(gregoryid, witcherid, '2022-11-30')
    l.printTable()
    l.returnBook(babiid, ayeletMetayeletid, '2023-08-14', '2023-08-17')
    l.returnBook(gregoryid, harryPotterid, '2023-08-27', '2023-09-05')
    l.returnBook(gregoryid, harryPotterid, '2023-06-22', '2023-06-23')
    l.returnBook(gregoryid, witcherid, '2022-11-30', '2022-12-07')

    l.printTable()

    l.lateLoans()
    # terminate connection and cursor
    infrastructure.disconnect()


