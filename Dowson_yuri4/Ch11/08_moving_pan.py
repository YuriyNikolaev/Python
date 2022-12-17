# filename 08_moving_pan.py
# Передвижная сковорода
# Демонстрирует ввод с помощью мыши

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite): # создаем класс Pan на базе Sprite
	""" Перемещаемая мышью сковорода. """
	def update(self): # переопределяем функцию upadate()
		""" Перемещает объект в позицию указателя."""
		self.x = games.mouse.x
		self.y = games.mouse.y

def main():
	wall_image = games.load_image("wall.jpg", transparent = False)
	games.screen.background = wall_image

	pan_image = games.load_image("pan.bmp") # вводим изображение
	the_pan = Pan(image = pan_image,
					x = games.mouse.x,
					y = games.mouse.y) # создаем объект Класса Pan
	games.screen.add(the_pan)  # дабвляем мыш на экран
	games.mouse.is_visible = False # убираем видимость указателя мыши
	games.screen.event_grab = True # перенаправояем ввод в графическое окно

	games.screen.mainloop()

if __name__ == '__main__':
	main()