# Filename PingPongCalculator_metr.py

#def convert_in2cm(inches):
#	return inches * 2.54

#def convert_lb2kg(pounds):
#	return pounds / 2.2

height_cm = int(input("Введите свой рост в сантиметрах: "))
weight_kg = int(input("Введите свой вес в килограммах: "))


ping_pong_tall = round(height_cm / 4)
ping_pong_heavy = round(weight_kg * 1000 / 2.7)

print("При росте", height_cm, "сантиметрах и весе", weight_kg, "килограмм") 
print("ваш рост", ping_pong_tall, "шариков для пинг-понга, а ")
print("вес сопоставим с", ping_pong_heavy, "шариков для пинг-понга!")