from mysql.connector import (connection)
#url = "10.10.103.252:3306/lib?allowPublicKeyRetrieval=true&useSSL=false"
login = 'user1'
password = '123456'

cnx = connection.MySQLConnection(user=login, password=password,
                                 host='10.10.103.252',
                                 database='lib')
def print_book_list():
    global cnx
    cursor = cnx.cursor()
    cursor.execute("select * from book")
    for line in cursor:
        print(line)
    cursor.close()

print_book_list()

cnx.close()