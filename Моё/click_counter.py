# click_counter.py
# счетчик щелчков

from tkinter import *

class Application(Frame):
	"""GUI-приложение для посчета нажатий кнопки"""

	def __init__(self, master):
		""" Инициализирует рамку."""
		super(Application, self).__init__(master)
		self.grid()
		self.bttn_clicks = 0 # кол-во нажатий
		self.create_widgets()

	def create_widgets(self):
		"""Создает кнопку, на которой
		отображается кол-во нажатий. """

		self.bttn = Button(self)
		self.bttn["text"] = "Количество щелчков: 0"
		self.bttn["command"] = self.update_count
		self.bttn.grid()

	def update_count(self):
		"""Увеличивает кол-во нажатий на единицу 
		и отображает его. """
		self.bttn_clicks += 1
		self.bttn["text"] = "Количество щелчков: " + str(self.bttn_clicks)

# основная часть
root = Tk()
root.title("Простейший GUI")
root.geometry("300x200")

app = Application(root)

# старт событийного окна
root.mainloop()	