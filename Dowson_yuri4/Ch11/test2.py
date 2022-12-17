# test2.py
# все тоже самое, только через класс
# пытаюсь собрать игру на основе того, что уже знаю

from livewires import games, color
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
	""" Перемещаемая мышью сковорода. """
	def update(self):
		""" Перемещает объект в позицию указателя."""
		self.x = games.mouse.x
		self.y = games.mouse.y
		self.check_collide()

	def check_collide(self):
		""" Проверяет, не соприкоснулись ли сковорода и пицца."""
		for pizza in self.overlapping_sprites:
			pizza.handle_collide()

class Pizza(games.Sprite):
	""" Скачущая пицца """
	#def update(self):
		"""Обращает одну или обе компоненты скорости, если
		достигнута граница экрана."""
	#	if self.right > games.screen.width or self.left < 0:
	#		self.dx = - self.dx

	#	if self.bottom > games.screen.height or self.top <0:
	#		self.dy = - self.dy

	def handle_collide(self):
		""" Перемещает спрайт в случайную позицию на графическом экране. """
		self.x = random.randrange(games.screen.width)
		self.y = random.randrange(games.screen.height)

		
def main():
	# установка фонового изображения
	wall_image = games.load_image("wall.jpg", transparent = False)
	games.screen.background = wall_image

	# вывод на экран пиццы
	pizza_image = games.load_image("pizza.bmp")
	#pizza = Pizza(image = pizza_image, 
	#				x = 100, 
	#				y = 100,
	#				dx = 1,
	#				dy = 1)
	pizza_x = random.randrange(games.screen.width)
	pizza_y = random.randrange(games.screen.height)
	pizza = Pizza(image = pizza_image, x = pizza_x, y = pizza_y)
	games.screen.add(pizza)

	# вывод счета на экран
	score = games.Text(value = 1756521,
					size = 60, 
					color = color.blue,
					x = 550,
					y = 30)
	games.screen.add(score)

	# Вывод на экран надписи "Победа!"
	won_message = games.Message(value = "Победа!",
							size = 100,
							color = color.red,
							x = games.screen.width/2,
							y = games.screen.height/2,
							lifetime = 250,
							#after_death = games.screen.quit
							)
	games.screen.add(won_message)

	# вывод мышки, в виде "передвижная сковорода""
	pan_image = games.load_image("pan.bmp")
	the_pan = Pan(image = pan_image,
					x = games.mouse.x,
					y = games.mouse.y)
	games.screen.add(the_pan)
	games.mouse.is_visible = False
	games.screen.event_grab = True
	


	games.screen.mainloop()


if __name__ == '__main__':
	main()

