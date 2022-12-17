# filename class_3.py

class Person:
	#конструктор
	def __init__(self, name):
		self.name = name # устанавливаем имя

	def __del__(self):
		print(self.name, "удален из памяти")

	def display_info(self):
		print("Привет, меня зовут", self.name)

person1 = Person("Tom")
person1.display_info() # Привет, меня зовут Tom
del person1  # удаление из памяти
person2 = Person("Sam")
person2.display_info() # Привет, меня зовут Sam