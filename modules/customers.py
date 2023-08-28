import infrastructure
class Customers (infrastructure.SqlInteraction):

    def __init__(self):
        #super().__init__()
        self.table = "Customers"

    def find(self, name):
        '''
        author: Gregory
        Date: 26/08/23
        :return: id of customer 'name'  from Customers
        '''

        self.name = name
        infrastructure.cursor.execute("select id from customers where Name = ?", (self.name))
        self.result = infrastructure.cursor.fetchall()[0][0]
        print ("id of customer "+self.name+" is "+str(self.result) )
        return (self.result)

    def addCustomer(self, name, city, age):
        '''
            author: Gregory
            Date: 26/08/23
            args: values of new customer to add
            action: inserts values to the customers table
        '''
        self.name = name
        # toAddLater: warning if there is a customer with same name
        self.city = city
        self.age = age
        # toAddLater: error message for unreasonable age input ( 120 < age < 5 )

        infrastructure.cursor.execute('insert into	customers values ( ?, ? , ? )', self.name, self.city, self.age)
        infrastructure.conn.commit()

        print ("customer "+self.name+" added")

    def removeCustomer (self, id):
        '''
            author: Gregory
            Date: 26/08/23
            id: id of customer to remove
            action: removes 'id' customer from customers table
        '''
        self.id = id
        # toAddLater: warning: are you shure?
        # toAddLater: warning if there is more than 1 customer with id customer's name
        infrastructure.conn.execute('delete from customers where id =  ?', self.id)
        infrastructure.conn.commit()

        print ("customer "+ str(self.id)+" removed")
