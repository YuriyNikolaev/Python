#test2.py
class Critter(object):
	"""Virt Pet """
	def __init__(self, name, mood):
		self.name = name
		self.__mood = mood
		print("Появилась зверюшка", self.name, "!")

	def __str__(self):
		rep = "Объект класса Critter\n"
		rep += "имя: " + self.name + "\n"
		return rep

	def talk(self):
		print("Привет. Меня зовут ", self.name)
		print("Сейчас я чувствую себя ", self.__mood)

	def __private_method(self):
		print("\nа затем Сработал закрытый метод")
	def public_method(self):
		print("\nСработал открытый метод")
		self.__private_method()

pet1  = input("Введите имя питомца1: ")
crit1 = Critter(pet1, mood = "прекрасно")
crit1.talk()
input("нажмите")
crit1.public_method()



print("\nВывод объекта crit1 на экран: ")
print(crit1)

print("\nНепосредственный доступ к атрибубу crit1.name:")
print(crit1.name)

input("\nenter чтобы выйти")
