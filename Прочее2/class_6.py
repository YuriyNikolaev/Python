# filename class_6.py
# инкапсуляция через определение свойств
class Person:
	#конструктор
	def __init__(self, name):
		self.__name = name # устанавливаем имя
		self.__age = 1

	@property  # свойство геттер или аксессор
	def age(self):
		return self.__age
	
	@age.setter  # свойство сеттер
	def age(self, age):
		if age in range(1, 100):
			self.__age = age
		else:
			print("Недопустимый возраст")

	@property
	def name(self):
		return self._name
	
	def display_info(self):
		print("Имя: ", self.__name, "\tВозраст: ", self.__age)

tom = Person("Tom")

tom.display_info()
tom.age = -3486
print(tom.age)
tom.age = 36
tom.display_info()