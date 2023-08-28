import infrastructure
import  pyodbc

class Books (infrastructure.SqlInteraction):
    def __init__(self):
        #super().__init__()
        self.table = "Books"

    def addBook(self,name,author,yearPublished,type):
        '''
            author: Gregory
            Date: 26/08/23
            args: values of new book to add
            action: inserts values to the books table
        '''
        self.name = name
        # toAddLater: warning if there is a book with same name
        self.author = author
        self.yearPublished = yearPublished
        # toAddLater: error message for unseasonable year input
        self.type = type
        # toAddLater: error message for type input other than possible ( 1/2/3 )
        infrastructure.cursor.execute('insert into	Books values ( ?, ? , ? , ?)',self.name, self.author, self.yearPublished, self.type)
        infrastructure.conn.commit()
        print ("book "+self.name+" added")

    def find(self, name):
        '''
        author: Gregory
        Date: 26/08/23
        return: returns the id of book 'name' from books
        '''

        self.name = name
        infrastructure.cursor.execute("select id from books where Name = ?", (self.name))
        self.result = infrastructure.cursor.fetchall()[0][0]
        print ("id of book "+self.name+" is "+str(self.result))
        return (self.result)

    def removeBook (self,id):
        '''
            author: Gregory
            Date: 26/08/23
            id: id of book to remove
            action: remuves 'id' book from books table
        '''
        self.id = id
        # toAddLater: warning: are you shure?
        infrastructure.conn.execute('delete from books where id =  ?', self.id)
        infrastructure.conn.commit()

        print("book " + str(self.id) + " removed")
