# app.py
# Expense Tracker
# RU URL: https://digitrain.ru/articles/164593/ 
# Git-Hub: https://github.com/Mozes721/Expense_Tracker

import db
from tkinter import *
from tkinter.ttk import *

LARGE_FONT = ("Verdana", 32)

class ExpenseTracker:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.main_window()

        # grid, labels, buttons wondows will come shortly after

### display function calls for database update deletion and listing added or deleted    
    def added(self, boxaile):
        myLabel = Label(boxaile, text='THe value has been inserted')
        myLabel.grid(row=4, column=0)

    def delete(self, boxaile):
        myLabel = Label(boxaile, text='The value was deleted')
        myLabel.grid(row=4, column=0)

    def display_all(self, database):
        select_all = database
        return select_all
    
    def insert(self, database, val1, val2, val3):
        goods = val1.get()
        price = val2.get()
        date = val3.get()
        insertion = database(goods, price, date)
        return insertion
    
    def find_expense(self, database, val1, val2):
        goods = val1.get()
        price = val2.get()
        find = database(goods, price)
        return find
    
    def delete_expense(self, database, val1, val2):
        goods = val1.get()
        price = val2.get()
        delete = database(goods, price)
        return delete
    
    ### MAIN WINDOW ###
    def main_window(self):
        button1 = Button(self.frame, text="Groceries expenses", command=self.groceries)
        button1.pack()

        button2 = Button(self.frame, text="Hosehold expenses", command=self.household)
        button2.pack()

        button3 = Button(self.frame, text="Entertament expenses", command=self.entertament)
        button3.pack()

        button4 = Button(self.frame, text="Other expenses", command=self.other)
        button4.pack()        

        button5 = Button(self.frame, text="EXIT", command=exit)
        button5.pack()  

    ### INSERT VALUES
    def groceries(self):

        top = Toplevel(self.frame)
        top.title('Groceries expense')
        l1 = Label(top, text="Name of good").grid(row = 1, column = 0, sticky = 2, pady = 2)
        l2 = Label(top, text="Price").grid(row = 2, column = 0, sticky = w, pady= 2)
        l3 = Label(top, text="Date of purchase").grid(row= 3, column= 0, sticky= w, pady= 2)

        e1 = Entry(top)
        e1.grid(row=1, column= 1, sticky= w, pady= 2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=w, pady=2)
        e3 = Entry(top)
        e3.grid(row=5, column=1, sticky=w, pady=2)

        text = Text(top, width=40, height=10)
        text.grid(row = 5, column =1, columnspan=2)

        #BUTTONS

        B1 = Button(top, text="Insert Values", command=lambda: (self.insert(db.insert_groceries, e1, e2, e3), self.added(top)))
        B1.grid(row=1, column=2)

        B2 = Button(top, text="Select All", command=lambda: (text.delete(1.0, END), text.insert(END, self.display_all(db.select_all_groceries()))))
        B2.grid(row=2, column=2)

        B3 = Button(top, text="Find value", command=lambda: (text.delete(1.0, END), text.insert(END, self.find_expense(db.select_grocery, e1, e2))))
        B3.grid(row=4, column=2)

        B3 = Button(top, text="Delete expense", command=lambda: (self.delete_expense(db.deltet_grocery, e1, e2), self.delete(top)))
        B3.grid(row=4, column=2)

        B5 = Button(top, text="Exit", command=exit)
        B5.grid(row=4, column=3)

    def household(self):
        top = Toplevel(self.frame)
        top.title('Household expenses')
        l1 = Label(top, text="Name of good").grid(row=1, column=0, sticky=w, pady=2)
        l2 = Label(top, text="Price").grid(row=2, column=0, sticky=w, pady=2)
        l3 = Label(top, text="Date of purchase").grid(row=3, column=0, sticky=w, pady=2)

        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=w, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=w, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=w, pady=2)

        text = Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        # BUTTONS #

        B1 = Button(top, text = "Insrt Values", 
            command=lambda: (self.insert(db.insert_houshold, e1, e2, e3), self.added(top)))
        B1.grid(row=1, column=2)

        B2 = Button(top, text="Select All", 
            command=lambda: (text.delete(1.0, END), text.insert(END, self.display_all(db.select_all_household()))))
        B2.grid(row=2, column=2)

        B3 = Button(top, text="Find value",
            command=lambda: (text.delete(1.0, END), text.insert(END, self.find_expense(db.select_household, e1, e2))))
        B3.grid(row=2, column=3)

        B3 = Button(top, text="Delete expense",
            command=lambda: (self.delete_expense(db.delete_household, e1, e2), self.delete(top)))
        B3.grid(row=4, column=2)

        B5 = Button(top, text="Exit", command=exit)
        B5.grid(row=4, column=3)

    def entertaiment(self):
        top = Toplevel(self.frame)
        top.title('Entertament expenses')
        l1 = Label(top, text="Name of good").grid(row=1, column=0, sticky=w, pady=2)
        l2 = Label(top, text="Price").grid(row=2, column=0, sticky=w, pady=2)
        l3 = Label(top, text="Date of purchase").grid(row=3, column=0, sticky=w, pady=2)

        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=w, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=w, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=w, pady=2)

        text = Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        # BUTTONS #
        B1 = Button(top, text = "Insrt Values", 
            command=lambda: (self.insert(db.insert_entertaiment, e1, e2, e3), self.added(top)))
        B1.grid(row=1, column=2)

        B2 = Button(top, text="Select All", 
            command=lambda: (text.delete(1.0, END), text.insert(END, self.display_all(db.select_all_entertaiment()))))
        B2.grid(row=2, column=2)

        B3 = Button(top, text="Find value",
            command=lambda: (text.delete(1.0, END), text.insert(END, self.find_expense(db.select_entertaiment, e1, e2))))
        B3.grid(row=2, column=3)

        B3 = Button(top, text="Delete expense",
            command=lambda: (self.delete_expense(db.delete_entertaiment, e1, e2), self.delete(top)))
        B3.grid(row=4, column=2)

        B5 = Button(top, text="Exit", command=exit)
        B5.grid(row=4, column=3)

    def other(self):
        top = Toplevel(self.frame)
        top.title('Entertament expenses')
        l1 = Label(top, text="Name of good").grid(row=1, column=0, sticky=w, pady=2)
        l2 = Label(top, text="Price").grid(row=2, column=0, sticky=w, pady=2)
        l3 = Label(top, text="Date of purchase").grid(row=3, column=0, sticky=w, pady=2)

        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=w, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=w, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=w, pady=2)

        text = Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        # BUTTONS #
        B1 = Button(top, text = "Insrt Values", 
            command=lambda: (self.insert(db.insert_other, e1, e2, e3), self.added(top)))
        B1.grid(row=1, column=2)

        B2 = Button(top, text="Select All", 
            command=lambda: (text.delete(1.0, END), text.insert(END, self.display_all(db.select_all_other()))))
        B2.grid(row=2, column=2)

        B3 = Button(top, text="Find value",
            command=lambda: (text.delete(1.0, END), text.insert(END, self.find_expense(db.select_other, e1, e2))))
        B3.grid(row=2, column=3)

        B3 = Button(top, text="Delete expense",
            command=lambda: (self.delete_expense(db.delete_other, e1, e2), self.delete(top)))
        B3.grid(row=4, column=2)

        B5 = Button(top, text="Exit", command=exit)
        B5.grid(row=4, column=3)



# the main finction will be at the end of the script
def main():
    # db.create_tables(connection)
    root = Tk()
    root.geometry('250x200')
    root.title("Expense Tracker")
    tracker = ExpenseTracker(root)

    root.mainloop()

main()