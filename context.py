from mysql.connector import (connection)

class Context:
    login = 'user1'
    password = '123456'
    def __init__(self):
        self.cnx = connection.MySQLConnection(user=self.login, password=self.password,
                                         host='10.10.103.252',
                                         database='lib')
        print("подключились к БД")
    def __del__(self):

    #    if self.cnx != None:
    #        self.cnx.close()
        print("отключились от БД")
