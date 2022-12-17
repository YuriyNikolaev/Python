# filename Dz4_autodealer.py
#
# соимость авто чистая
clear_coast = int(input("\nВведите соимость автомобиля, руб.: "))
nalog = 0.18 * clear_coast
reg_sbor =  0.05 * clear_coast
agent_sbor = 300
dostavka =  1000

total_coast = clear_coast + nalog + reg_sbor + agent_sbor + dostavka
print("\nИтого машина в круг ", total_coast, "руб.")
print("\nИз них Налог: ", nalog, " руб.")
print("Рег сбор: ", reg_sbor, " руб.")
print("Агентский сбор: ", agent_sbor, " руб.")
print("Доставка: ", dostavka, "руб.")
print("\nИтого: ", total_coast, " руб.")

# Выход
input("\nНажмите Ентер шобы выйти!")