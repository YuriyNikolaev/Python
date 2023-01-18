import random

player_score, computer_score = 0, 0

while player_score < 3 and computer_score < 3:
	print("-" * 50)
	player_motion = input("Игрок показывает: ")
	if player_motion not in ["к", "б", "н"]:
		print("Неверный ход")
		continue

	computer_motion = random.choice(("к", "б", "н"))
	print("Компьютер выкидывает: ", computer_motion)

	if player_motion == computer_motion:
		print("Ничья")
	elif any((player_motion == "к" and computer_motion == "н",
			  player_motion == "н" and computer_motion == "б",
			  player_motion == "б" and computer_motion == "к")):
		print("Партию выиграл игрок")
		player_score += 1
	else:
		print("Партия за компом")
		computer_score += 1

print("Победил", "игрок" if player_score == 3 else "компьютер", end="!\n")