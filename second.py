from context import Context

context = Context()

def print_book_list():
    global context
    cursor = context.cnx.cursor()
    cursor.execute("select * from book")
    for line in cursor:
        print(line)
    cursor.close()

#создать функцию, которая выводит информацию обо всех книгах определенного автора

# создать функцию, которая получает книги определенного автора в виде списка
def get_books_by_author(name: str)->list:
    result=[]
    global context
    cursor = context.cnx.cursor()
    query = "select b.* " \
            "from book b join authorship a " \
            "on b.isbn = a.isbn "\
            "join author a2 "\
            "on a.id_author =a2.id " \
            "where fio like %s"
    cursor.execute(query, (name,))
    for line in cursor:
        result.append(line)
    cursor.close()
    return result

def print_books_by_author(name:str):
    print('---все книги от автора----')
    print(name)
    books = get_books_by_author(name)
    print(books)
    print('--------------------------')


#print_book_list()
print_books_by_author('Пушкин')
print_books_by_author('Толкин')

context.cnx.close()