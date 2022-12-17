# Filename 31_RosettesAndPolygons.py - спираль из многоугольников
# И розеток!
import turtle
t = turtle.Pen()
t.speed(0) # сам добавил
# Запросить у пользователя количество сторон, по умолчанию 4
sides = int(turtle.numinput("Количество сторон", "Сколько сторон будет \
	у вашей спирали?", 4))
# Внешний цикл для многоугольников и розеток, размер от 5 до 75
for m in range(5, 75):
	t.left(360/sides + 5)
	t.width(m//25 + 1)
	t.penup() # Не рисовать линии спирали
	t.forward(m*4) # Перейти к следующему углу
	t.pendown() # Приготовиться к рисованию
	# Нарисовать небольшую розетку на каждлм ЧЕТНОМ углу
	# спирали
	if (m % 2 == 0):
		for m in range(sides):
			t.circle(m/3)
			t.right(360/sides)
			# ИЛИ, нарисовать небольшой многоугольник
			# на каждом НЕЧЕТНОМ углу
	else:
		for n in range(sides):
			t.forward(m)
			t.right(360/sides)
