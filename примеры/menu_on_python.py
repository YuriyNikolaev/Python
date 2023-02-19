# Создание Menu на языке Python

from tkinter import *
root = Tk()


def func1():              # создание нового окна
    win = Toplevel(root)


def func2():              # нажатие закрыть
    root.destroy()
    lab = label(root, text="метод add_cascade добавляет пункт нового меню")  #
    lab.pack()


m = Menu(root)
root.config(menu=m)

mm1 = Menu(m)
m.add_cascade(label="Файл", menu=mm1)
mm1.add_command(label="Новый файл", command=func1)
mm1.add_command(label="Открыть")
mm1.add_command(label="Закрыть", command=func2)

mm2 = Menu(m)
m.add_cascade(label="Правка", menu=mm2)
mm2.add_command(label="Копировать")
mm2.add_command(label="Вставить")

root.mainloop()
