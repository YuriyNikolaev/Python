# filename 07_critter_caretaker_v2.py
# новая зверюшка
# 1 пользователь сам решает сколько еды дать
# 2 сколько времени играть
# 3 зверюшка насыщается и веселеет в зависимости
# от этих параметров

class Critter(object):
	"""Virtual Pet """
	def __init__(self, name, hunger = 0, boredom = 0):
		self.name = name
		self.hunger = hunger # уровень голода
		self.boredom = boredom # уровень уныния
		

	def __pass_time(self):
		self.hunger += 1
		self.boredom += 1

	@property
	def mood(self):  # уровень настроения
		unhappieness = self.hunger + self.boredom
		if unhappieness < 5:
			m = "прекрасно"
		elif 5<= unhappieness <= 10:
			m = "неплохо"
		elif 11<= unhappieness <= 15:
			m = "не сказать ,чтобы хорошо"
		else:
			m = "ужасно"
		return m

	def talk(self): # сообщение от зверюшки
		print("меня зовут ", self.name, ", и сейчас я себя чувствую", self.mood, "\n")
		self.__pass_time()

	# питание
	def eat(self, food): 
		
		print("Мрр... Спасибо!")
		print("Зверюшка покормлена на ", food, "единиц еды.")
		self.hunger -= food
		if self.hunger <0:
			self.hunger = 0
		print("Уровень голода ", self.hunger)
		self.__pass_time()

	def play(self, fun): # игра
		print("Уиии!")
		print("зверюшка наиграна на", fun, "единиц")
		self.boredom -= fun
		if self.boredom <0:
			self.boredom = 0
		print("уровень скуки ", self.boredom)
		self.__pass_time()

def main():
	crit_name = input("Как назовете свою зверюшку?: ")
	crit = Critter(crit_name)

	choice = None
	while choice != "0":
		print \
		("""
		Моя зверюшка
		0 - Выйти
		1 - Узнать о самочувствии зверюшки
		2 - Покормить зверюшку
		3 - Поиграть со зверюшкой
		""")
		choice = input("Ваш выбор: ")
		print()
		# exit
		if choice == "0":
			print("До свидания.")
		# беседа со зверюшкой
		elif choice == "1":
			crit.talk()
		# кормление зверюшки
		elif choice == "2":
			food = int(input("Введите кол-во еды (от 0 до 4): "))
			if 0 <= food <= 4:
				crit.eat(food)
			else:
				print("Не знаю такого числа")
		elif choice == "3":
			fun = int(input("Введите число для игры (от 0 до 4): "))
			if 0 <= fun <= 4: 
				crit.play(fun)
			else:
				print("Не знаю такого числа")
		# не понятный пользотваельский ввод	
		else:
			print("Извините, в меню нет пункта", choice)

main()
input("\n\nНажмите Enter, чтобы выйти.")




		
	

