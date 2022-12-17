# Filename Test.py

from tkinter import *

# создание базового окна
from tkinter import Frame

root  = Tk()

# изменение окна
root.title("Простейший GUI")
root.geometry("300x200")

# внутри окна создается рамка для размещения других элементов
app = Frame(root)
app.grid()

# создание метки внутри рамки
lbl = Label(app, text = "Это метка. Вот она я!")
lbl.grid()

# кнопки внутри рамки
bttn1 = Button(app, text = "Кнопка1 Я ничего не делаю.")
bttn1.grid()

# вторая кнопка внутри рамки
bttn2 = Button(app)
bttn2.configure(text = "Кнопка2 Я тоже ничего не делаю!")
bttn2.grid()

# третья кнопка
bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "Кнопка 3 И я!"

# старт событийного окна
root.mainloop()