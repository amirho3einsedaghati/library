import sqlite3


def connect():
    connection = sqlite3.connect("bookStore.db")
    cur = connection.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, bookTitle text, authorName text, year text, ISBN INTEGER)")
    connection.commit()
    connection.close()


def insert(bookTitle,authorName,year,ISBN):
    connection = sqlite3.connect("bookStore.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO book VALUES(NULL , ?, ?, ?, ?)",(bookTitle,authorName,year,ISBN))
    connection.commit()
    connection.close()


def select_all():
    connection = sqlite3.connect("bookStore.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM book")
    received_rows= cur.fetchall()
    connection.commit()
    connection.close()
    return received_rows


def update(id,bookTitle,authorName,year,ISBN):
    connection = sqlite3.connect("bookStore.db")
    cur = connection.cursor()
    cur.execute("UPDATE book SET bookTitle=?, authorName=?, year=?, ISBN=? where id=?",(bookTitle,authorName,year,ISBN,id))
    connection.commit()
    connection.close()


def search(bookTitle="",authorName="",year="",ISBN=""):
    connection = sqlite3.connect("bookStore.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM book WHERE bookTitle=? OR authorName=? OR year=? OR ISBN=?",(bookTitle,authorName,year,ISBN))
    received_rows= cur.fetchall()
    connection.commit()
    connection.close()
    return received_rows


def delete(id):
    connection=sqlite3.connect("bookStore.db")
    cur=connection.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    connection.commit()
    connection.close()


connect()





# insert(,1999,89124379"شمس","مولانا",)
# insert("1,2,3 بدرخش","shahab anari",2018,91827901)
# insert("سفر کوانتومی وال تنها","iman sarvarpour",2021,18230129)
# insert("تمام جهان در من است","iman sarvarpour",2018,19823712039)

# print(select_all())

# update(5,"انسان در جستجوی معنا","victor frankl",1999,89124379)
# update(9,"شمس","molana",1999,89124379)

# print(search(bookTitle="انسان در جستجوی معنا"))
# print(search(authorName="iman sarvarpour"))

# delete(9)