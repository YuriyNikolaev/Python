# 2_3_3-3.py

# Дан список
l = [2,4,6,7,10,12,14,16]
print(l)

#  1) Заменил второй элемент списка на 0;
l.pop(1)
l.insert(1, 0)
print(l)

# Добавил числа 1, 2 и 3 в конец списка;
l.append(1)
l.append(2)
l.append(3)
print(l)

# Удвоить список
l.extend(l)
print(l)