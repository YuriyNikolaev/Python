# сколько учеников в каждом классе
classA = int(input('Учеников в классе А: '))
classB = int(input('Учеников в классе B: '))
classC = int(input('Учеников в классе C: '))

# парт на 1н класс
# кол-во учеников / 2
partsClassA = classA // 2
partsClassB = classB // 2
partsClassC = classC // 2

print("Парт для учеников класса А", partsClassA)
print("Парт для учеников класса В", partsClassB)
print("Парт для учеников класса С", partsClassC)

# количество парт
total =  partsClassA + partsClassB + partsClassC

print('Всего нужно ', total, ' парт')