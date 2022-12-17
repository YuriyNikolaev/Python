# filename 05_simple_game.py
# Простая игра
# Демонстрирует импорт модулей
import games, random

print("Добро пожаловать в самую-самую простую игру!\n")
again = None
while again != "n":
	players = [] # создаем пустой список игроков
	# спрашиваем сколько игроков будет играть
	# помещаем это значение в num
	num = games.ask_number(question = "Сколько игроков участвует? (2-5): ", low = 2, high = 5)

	# цикл: спрашиваем имя каждого игрока и генерируем число
	for i in range(num):
		name = input("Имя игрока: ") # спршиваем имя
		score = random.randrange(100) + 1 # генерируем случайное число
		player = games.Player(name, score) # создаем игрока, присваиваем ему имя и сгенерированное число
		players.append(player) # добавляем игрока в списрк игроков

	print("\nВот результаты игры: ") # выводим результат игры через цикл
	for player in players:
		print(player)

	again = games.ask_yes_no("\nХотите сыграть еще раз? (y/n): ")

input("\n\nНажмите Enter, чтобы выйти.")