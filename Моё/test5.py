# test5.py
# применение флажков

from tkinter import *

class Aplication(Frame):
	""" GUI-приложение """
	def __init__(self, master):
		super(Aplication, self).__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		""" Создает элементы """
		# создает метку-описание
		Label(self,
			text = "Метка-описание"
			).grid(row = 0, column = 0, sticky = W)
		
		# переменная для хранения сведений о выборе жанра
		self.favorite = StringVar()
		self.favorite.set(None)

		# положение "Комедия" переключателя
		Radiobutton(self,
			text = "Комедия",
			variable = self.favorite,
			value = "комедия",
			command = self.update_text
			).grid(row = 2, column = 0, sticky = W)

		# положение "Драма" переключателя
		Radiobutton(self,
			text = "Драма",
			variable = self.favorite,
			value = "Драма",
			command = self.update_text
			).grid(row = 3, column = 0, sticky = W)

		# флажок "Фильмы о любви"
		self.likes_romance = BooleanVar()
		Checkbutton(self,
			text = "Фильмы о любви",
			variable = self.favorite,
			command = self.update_text
			).grid(row = 4, column = 0, sticky = W)

		# текстовая область с результатом
		self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
		self.results_txt.grid(row = 5, column = 0, columnspan = 3)

	def update_text(self):
		""" Обновляет текстовую область """
		message = "Ваш любимый киножанр - "
		message += self.favorite.get()

		if self.likes_romance.get():
			message += " кино о любви."

		self.results_txt.delete(0.0, END)
		self.results_txt.insert(0.0, message)




# main part
root = Tk()
root.title("Применение флажков")
app = Aplication(root)
root.mainloop()