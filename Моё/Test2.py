# Filename Test2.py
# делаем кнопки через классы
# бесполезные кнопки вариант 2

from tkinter import *

class Application(Frame):
	""" GUI приложение с тремя кнопками. """

	def __init__(self, master):
		""" Инициализирует рамку. """
		super(Application, self).__init__(master)
		self.grid()
		self.creat_widgets()

	def creat_widgets(self):
		""" Создает три бесполезные кнопки. """
		# первая кнопка
		self.bttn1 = Button(self, 
			text = "Кнопка1 Я ничего не делаю.")
		self.bttn1.grid()
		
		# вторая кнопка
		self.bttn2 = Button(self)
		self.bttn2.grid()
		self.bttn2.configure(text = "Кнопка2")

		# третья кнопка
		self.bttn3 = Button(self)
		self.bttn3.grid()
		self.bttn3["text"] = "Кнопка3"


# основная часть
root = Tk()
root.title("Простейший GUI")
root.geometry("300x200")

app = Application(root)

lbl = Label(app, text ="Это метка. Вот она я!")
lbl.grid()

lbl2 = Label(app, text ="Вторая метка.")
lbl2.grid()

# старт событийного окна
root.mainloop()