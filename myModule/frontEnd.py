# =================================================== Start: UI_bookStore =============================================
from tkinter import *
import backEnd

window = Tk()
window.title("Book Store")


# --------------------------------
# these functions are related to repetitive actions.

def delete_books():
    lb.delete(0, END)


def fill_list_box(books):
    for book in books:
        lb.insert(END, book)


# ==================================== Labels ==============================
l1 = Label(window, text="Book Title")
l1.grid(row=0, column=0)

l1 = Label(window, text="Author Name")
l1.grid(row=0, column=2)

l1 = Label(window, text="Year")
l1.grid(row=1, column=0)

l1 = Label(window, text="ISBN")
l1.grid(row=1, column=2)

# ==================================== Entries ==============================
bookTitle = StringVar()
e1 = Entry(window, textvariable=bookTitle)
e1.grid(row=0, column=1)

authorName = StringVar()
e2 = Entry(window, textvariable=authorName)
e2.grid(row=0, column=3)

year = StringVar()
e3 = Entry(window, textvariable=year)
e3.grid(row=1, column=1)

isbn = StringVar()
e4 = Entry(window, textvariable=isbn)
e4.grid(row=1, column=3)

# ==================================== ListBox and Scroll ==============================
lb = Listbox(window, width=60, height=8)
lb.grid(row=2, column=0, rowspan=6, columnspan=2)

sc = Scrollbar(window)
sc.grid(row=2, column=2, rowspan=6)

lb.configure(yscrollcommand=sc.set)
sc.configure(command=lb.yview)


def get_selected_book(evnet):
    global selected_row
    if len(lb.curselection()) > 0:
        index = lb.curselection()[0]
        # print(index)
        selected_row = lb.get(index)
    # Book Title
    e1.delete(0, END)
    e1.insert(END, selected_row[1])
    # Author Name
    e2.delete(0, END)
    e2.insert(END, selected_row[2])
    # Year
    e3.delete(0, END)
    e3.insert(END, selected_row[3])
    # ISBN
    e4.delete(0, END)
    e4.insert(END, selected_row[4])


lb.bind("<<ListboxSelect>>", get_selected_book)


# ==================================== Buttons and their Functionality ==============================
def view_command():
    delete_books()
    books = backEnd.select_all()
    fill_list_box(books)


b1 = Button(window, text="View All", width=12, command=lambda: view_command())
b1.grid(row=2, column=3)


# --------------------------------------------------
def search_command():
    delete_books()
    books = backEnd.search(bookTitle=bookTitle.get(), authorName=authorName.get(), year=year.get(), ISBN=isbn.get())
    fill_list_box(books)


b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)


# --------------------------------------------------
def send_entries_value_to_insert():
    backEnd.insert(bookTitle=bookTitle.get(), authorName=authorName.get(), year=year.get(), ISBN=isbn.get())
    view_command()


b3 = Button(window, text="Add Entry", width=12, command=lambda: send_entries_value_to_insert())
b3.grid(row=4, column=3)


# --------------------------------------------------
def update_command():
    backEnd.update(selected_row[0], bookTitle=bookTitle.get(), authorName=authorName.get(), year=year.get(),
                   ISBN=isbn.get())
    view_command()


b4 = Button(window, text="Update Selected", width=12, command=update_command)
b4.grid(row=5, column=3)


# --------------------------------------------------
def delete_command():
    backEnd.delete(selected_row[0])
    view_command()


b5 = Button(window, text="Delete Selected", width=12, command=lambda: delete_command())
b5.grid(row=6, column=3)

# --------------------------------------------------
b6 = Button(window, text="Close", width=12, command=lambda: window.destroy())
b6.grid(row=7, column=3)

# ==================================== End ==============================

view_command()
window.mainloop()
