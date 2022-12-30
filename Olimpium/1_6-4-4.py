# # Константы для хранения цен на разные категории билетов
# BABY_PRICE = 0.00
# CHILD_PRICE = 14.00
# ADULT_PRICE = 23.00
# SENIOR_PRICE = 18.00
# # Сохраним как константы возрастные ограничения
# BABY_LIMIT = 2
# CHILD_LIMIT = 12
# ADULT_LIMIT = 64
# # Переменная для хранения общей суммы посещения
# total = 0
# # Читаем ввод пользователя до пустой строки
# line = input("Введите возраст посетителя (пустая строка для окончания ввода): ")
# while line != "":
#  age = int(line)
#  # Добавляем цену билета к общей сумме
#  if age <= BABY_LIMIT:
#     total = total + BABY_PRICE
#  elif age <= CHILD_LIMIT:
#     total = total + CHILD_PRICE
#  elif age <= ADULT_LIMIT:
#     total = total + ADULT_PRICE
#  else:
#     total = total + SENIOR_PRICE
#  # Считываем возраст следующего посетителя
#  line = input("Введите возраст посетителя (пустая строка для окончания ввода): ")
# # Отображаем сумму группового посещения с правильным форматированием
# print("Сумма посещения зоопарка для этой группы составит $%.2f" % total)

# 1_6-4-4.py
# мой варианти
age = input("Введите возраст посетителя (Enter, чтобы закончить ввод)")

total = 0 # начальная цена

while age != '':
    age = int(age)
    if age in range(0, 2):
        price = 0
    elif age in range(3, 12):
        price = 14
    elif age > 65:
        price = 18
    else:
        price = 23
    
    total = total + price
    
    age = input("Введите возраст посетителя (Enter, чтобы закончить ввод)")
    
print(total)  