# Test3.py
# пробую вставлять кнопки

from tkinter import *

class Application(Frame):
	"""GUI-приложение. """
	def __init__(self, master):
		""" Инициализирует рамку """
		super(Application, self).__init__(master)
		self.grid()
		self.bttn_clicks = 0
		self.create_widgets()

	def create_widgets(self):
		""" Создает кнопку, текстовой поле и текстовую область."""

		# создается метка-инструкция
		self.inst_lbl = Label(self, text = "Метка-инструкция")
		self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

		# создается метка около поля ввода
		self.pw_lbl = Label(self, text = "Метка около поля ввода ПАРОЛЯ: ")
		self.pw_lbl.grid(row = 1, column = 0, sticky = W)

		# создается текстовое поле вводы пароля
		self.pw_ent = Entry(self)
		self.pw_ent.grid(row = 2, column = 1, sticky = W)

		# создается кнопка отправки значений
		self.bttn_clicks += 1
		self.submit_bttn = Button(self, text = "Секреты узнать" + str(self.bttn_clicks), command = self.reveal)
		self.submit_bttn.grid(row = 2, column = 0, sticky = W)

		# создание текстовой области, в которую будет введен ответ
		self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
		self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)


	def reveal(self):
		#pass
		contents = self.pw_ent.get()
		if contents == "secret":
			message = "Какое то сообщение"
		else:
			message = "что-то пошло не так"
		self.secret_txt.delete(0.0,END)
		self.secret_txt.insert(0.0, message)

# основная часть
root = Tk()
root.title("Пробы с сеткой")
root.geometry("400x150")
app = Application(root)
root.mainloop()