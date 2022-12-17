# filename private_critter.py
# Закрытая зверюшка
# Демонстрирует закрытые переменные и методы
class Critter(object):
	"""Виртуальный питомец"""
	def __init__(self, name, mood):
		print("Появилась на свет новая зверюшка!")
		self.name = name # Открытый атрибут
		self.__mood = mood   # закрытый атрибут
	def talk(self):
		print("\nМеня зовут", self.name)
		print("Сейчас я чувствую себя", self.__mood, "\n")
	def __private_method(self): # закрытый метод.
		print("Это закрытый метод.")
	def public_method(self):  	# открытый метод
		print("Это открытый метод.")
		self.__private_method()

# основная часть
crit = Critter(name = "Бобик", mood = "прекрасно")
input("нажмите")
crit.talk()
input("нажмите")
crit.public_method()

input("\n\nНажмите Enter, чтобы выйти.")
