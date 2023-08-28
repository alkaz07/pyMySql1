from context import Context

context = Context()

def add_author(name:str)->int:
    global context
    cursor = context.cnx.cursor()
    cursor.execute("INSERT INTO author(fio) VALUES (%s);", (name,))
    cursor.execute("SELECT last_insert_id();")
    x = cursor.fetchone()[0]
    cursor.close()
    return x

print('добавляем автора XXZ и получаем:')
print(add_author('XXZ'))

