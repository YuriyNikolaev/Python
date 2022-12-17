# filename property_critter.py
# Зверюшка со свойствами
# Демонстрирует свойства
class Critter(object):
	"""Виртуальный питомец"""
	def __init__(self, name):
		print("Появилась на свет новая Зверюшка!")
		self.__name = name
	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self, new_name):
		if new_name == "":
			print("Имя зверюшки не может быть пустой строкой.")
		else:
			self.__name = new_name
			print("Имя изменено.")
	def talk(self):
		print("\nПривет, меня зовут", self.name)

# основная часть 
crit = Critter("Бобик")
input("нажмите")
crit.talk()

input("нажмите")

print("\nМою зверюшку зовут", end="")
print(crit.name)

input("нажмите")

print("\nПопробую изменить имя зверюшки на Мурзик...")
crit.name = "Мурзик"

input("нажмите")

print("\nМою зверюшку зовут", end="")
input("\nнажмите")
print(crit.name)
# Появится текст 'Мою зверюшку зовут Мурзик'
# Теперь преприму попытку заменить имя зверюшки на пустую строку:

input("\nнажмите")

print("\nПопробую изменить имя зверюшки на пустую строку...")
input("\nнажмите")
crit.name = ""

print("\nМою зверюшку зовут", end="")
input("нажмите")
print(crit.name)
# компьютер скажет нам, что имя зверька все еще Мурзик.
input("нажмите")

input("\n\nНажмите Enter, чтобы выйти.")