# test4.py

from tkinter import *

class Application(Frame):
	"""GUI-приложение"""
	def __init__(self, master):
		super (Application, self).__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		"""Создает элементы """

		# создается метка-описание
		Label(self,
			text = "Это Метка-описание"
			).grid(row = 0, column = 0, sticky = W)
		
		# создается метка-инструкция
		Label(self,
			text = "Это Метка-инструкция: "
			).grid(row = 1, column = 0, sticky = W)

		# флажок комедия
		self.likes_comedy = BooleanVar()
		Checkbutton(self,
			text = "Комедия",
			variable = self.likes_comedy,
			command = self.update_text
			).grid(row = 2, column = 0, sticky = W)

		self.results_text = Text(self, width = 40, height = 5, wrap = WORD)
		self.results_text.grid(row = 5, column = 0, columnspan = 3)

	def update_text(self):
		""" Обновляет текстовый элемент """
		likes = ""
		if self.likes_comedy.get():
			likes += "Вам нравится комедии.\n"
		self.results_text.delete(0.0, END)
		self.results_text.insert(0.0, likes)



# основная часть
root = Tk()
root.title("Демонстрация флажков")
app = Application(root)
root.mainloop()