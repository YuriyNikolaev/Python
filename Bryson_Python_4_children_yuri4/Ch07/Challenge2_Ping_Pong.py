# Filename Challenge2_Ping_Pong.py

# Программа высчитывает высоту и вес введенного юзером кол-ва шариков
# для пинг-понга

number_ping_pong = int(input("Введите количество шариков: "))

height_cm = number_ping_pong * 4
weight_kg = number_ping_pong * 2.7 / 1000

print("Высота", number_ping_pong, " шариков составит", height_cm, "см.")
print("Вес", number_ping_pong, "шариков составит ", weight_kg, "кг." )
