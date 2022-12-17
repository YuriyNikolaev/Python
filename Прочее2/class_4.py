# filename class_4.py
# атрибуты класса общедоступны
class Person:
	#конструктор
	def __init__(self, name):
		self.name = name # устанавливаем имя
		self.age = 1

	def display_info(self):
		print("Имя: ", self.name, "\tВозраст: ", self.age)

tom = Person("Tom")
tom.name = "Человек-паук" # изменяем атрибут name
tom.age = -129			  # изменяем атрибут age
tom.display_info()        # Имя: Человек-паук