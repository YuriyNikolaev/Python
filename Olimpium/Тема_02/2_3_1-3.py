# 2_3_1-3.py


# Допиши программу, обрабатывающую список учеников. Она должна:
# 1. Считать число учеников в классе.
# 2. «Красиво» выводить пронумерованный список.
# 3. На вход программе подается одно число m. 
# Напишите программу, которая выводит список [1, 2, 3, …, m].
# 4. Задать числовой список случайным образом. 
# Заменить значение элементы в списке на их квадраты.
my_class = ["Петров", "Иванов", "Сидоров", "Коновалов"]

print("Мой класс ", my_class)


# 1. Считать число учеников в классе.
print("Число учеников в классе = ", len(my_class))


# 2. «Красиво» выводить пронумерованный список.
for i in range(0, len(my_class)):
    print(i,'. ' ,my_class[i])

# 3. На вход программе подается одно число m. 
# Напишите программу, которая выводит список [1, 2, 3, …, m].
m = 4
i = 0
while i < m:    
    print(i + 1,'. ', my_class[i])
    i += 1

# 4. Задать числовой список случайным образом. 
# Заменить значение элементы в списке на их квадраты.