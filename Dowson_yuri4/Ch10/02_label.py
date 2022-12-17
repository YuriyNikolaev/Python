# filename 02_label.py
# Это я, метка
# Демонстрирует применение меток
from tkinter import *

# создание базового окна
root = Tk()
root.title("Метка на рамке.") # метка на рамке
root.geometry("300x100")

# внутри окна создается рамка для размещения других элементов
app = Frame(root)
app.grid()

# создание метки внутри рамки
lbl = Label(app, text = "Метка внутри рамки.")
lbl.grid()

# старт событийного цикла
root.mainloop()