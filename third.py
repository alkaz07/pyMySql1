from context import Context
from book import Book

context=Context()
def get_books_by_author(name: str)->list[Book]:
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

   # for line in cursor:
    #    book = Book(line[0],line[1], line[2], line[3])
     #   result.append(book)
    for (i, t, y, p) in cursor:
        book = Book(i, t, y, p)
        result.append(book)
    cursor.close()
    return result

def print_book_list_by_author(name:str):
    print(f'------список книг автора {name} ------------')
    books = get_books_by_author(name)
    for b in books:
        print(f' {b.isbn} \t {b.title} \t {b.year} \t {b.publisher}')
    print('---------------------------------------------')

print_book_list_by_author('Толстой')
print_book_list_by_author('Сапковский')

context.cnx.close()