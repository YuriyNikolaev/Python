# longevity.py

from tkinter import *

class Application(Frame):
	"""GUI-приложение """
	def __init__(self, master):
		"""Инициализирует рамку """
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		""" Создает кнопку, текстовое поле, текстовую область. """
		# метка-инструкция
		self.inst_lbl = Label(self, text = "Чтобы узнать секрет долголетия, введите пароль.")
		self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

		# метка около поля ввода пароля
		self.pw_lbl = Label(self, text = "Пароль: ")
		self.pw_lbl.grid(row = 1, column = 0, sticky = W)

		# текстовое поле для ввода пароля
		self.pw_ent = Entry(self)
		self.pw_ent.grid(row = 1, column = 1, sticky = W)

		# кнопка отправки значения
		self.submit_bttn = Button(self, text = "Узнать секрет", command = self.reveal)
		self.submit_bttn.grid(row = 2, column = 0, sticky = W)

		# создание текстовой области, в которую будет введен ответ
		self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
		self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

	def reveal(self):
		""" В зависимости от введеного пароля отвечает разными сообщениями."""
		contents = self.pw_ent.get()

		if contents == "secret":
			message = "Чтобы дожить до 100 лет, надо сначала дожить до 99, " \
			"а потом вести себя ОЧЕНЬ осторожно."
		else:
			message = "Вы ввели не правильный пароль."
		self.secret_txt.delete(0.0, END)
		self.secret_txt.insert(0.0, message)

# основная часть 
root = Tk()
root.title("Долгожитель")
root.geometry("300x150")
app = Application(root)
root.mainloop()