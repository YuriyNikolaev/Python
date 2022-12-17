# filename 01_simple_gui.py
# Простейший GUI
# Демонстрирует создание окна
from tkinter import *

# создание базового окна
root = Tk()

# изменение окна
root.title("Простейший GUI")
root.geometry("300x100")

# старт событийного окна
root.mainloop()