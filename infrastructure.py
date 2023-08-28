import pyodbc
#open connection and cursor
# toAddLater: try and catch
conn = pyodbc.connect('Driver=SQL Server Native Client 11.0;server=DESKTOP-RT6RSES\SQLEXPRESS01;Database=GregoryBooksLibrary;Trusted_Connection=yes')
cursor = conn.cursor()
print ("connected to database")

def disconnect ():
    '''
    author: Gregory
    Date: 26/08/23
    action : terminates connection and sursor
    '''
    cursor.close()
    conn.close()
    print("disconnected from database")

class SqlInteraction (object):
    '''
    the parent class that defines the generic interactions with GregoryBooksLibrary database
    '''
    def printTable(self):
        '''
            author: Gregory
            Date: 26/08/23
            :return: prints the relevant table
        '''

        print (self.table+ " table:")
        cursor.execute("select * from "+self.table)
        self.result = cursor.fetchall()
        for row in self.result:
            print(row)
            print("\n")

        print('_______________________')
