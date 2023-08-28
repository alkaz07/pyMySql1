from context import Context

context = Context()


def add_author(name: str) -> int:
    global context
    cursor = context.cnx.cursor()
    cursor.execute("INSERT INTO author(fio) VALUES (%s);", (name,))
    context.cnx.commit()
    cursor.execute("SELECT last_insert_id();")
    x = cursor.fetchone()[0]
    cursor.close()
    return x


# добавление читателя вызовом ХП
def add_reader(name: str) -> int:
    global context
    cursor = context.cnx.cursor()
    cursor.callproc('ins_reader1', (name,))
    context.cnx.commit()
    cursor.execute("SELECT last_insert_id();")
    x = cursor.fetchone()[0]
    cursor.close()
    return x


# написать функцию выдачи книги по названию и nchit
def vydat_book(title: str, nchit: int):
    global context
    cursor = context.cnx.cursor()
    # применяем ХП с параметрами
    cursor.callproc('vydat_book', (nchit, title))
    context.cnx.commit()
    # применяем представление, добавляя параметры фильтрации
    q = "SELECT nchit, fio, date_out, date_in, id_ex, title FROM lib.kto_chto_kogda_bral " \
        "WHERE nchit= %s AND title= %s"
    cursor.execute(q, (str(nchit), title))
    for line in cursor:
        print('выдано: ',line)
    cursor.close()


# print('добавляем автора XXZ и получаем:')
# print(add_author('XXZ'))

#print('добавляем читателя ZZZZ и получаем:')
#print(add_reader('ZZZZ'))

vydat_book('Три мушкетера',2024 )