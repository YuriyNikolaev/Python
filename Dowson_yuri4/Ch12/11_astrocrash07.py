# filename 11_astrocrash07.py
# Прерванный полет 7
# обработка взрывов
from livewires import games
import math, random

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Wrapper(games.Sprite):
	"""Огибатель. Спрайт, который, двигаясь, огибает графический экран. """
	def update(self):
		""" Переносит спрайт на противоположную сторону экрана. """
		if self.top > games.screen.height:
			self.bottom = 0
		
		if self.bottom < 0:
			self.top = games.screen.height
		
		if self.left > games.screen.width:
			self.right = 0
		
		if self.right < 0:
			self.left = games.screen.width

	def die(self):
		"""Разрушает объект."""
		self.destroy()

class Collider(Wrapper):
	"""Погибатель. Огибатель, который может столкиваться с другими объектами
	и гибнуть. """
	def update(self):
		""" Проверяет, нет ли спрайтов, визуально перекрывающихся с данным."""
		super(Collider, self).update()

		if self.overlapping_sprites:
			for sprite in self.overlapping_sprites:
				sprite.die()
			self.die()

	def die(self):
		""" Разрушает объект со взрывом."""
		new_explosion = Explosion(x = self.x, y = self.y)
		games.screen.add(new_explosion)
		self.destroy()

class Asteroid(Wrapper):
	"""Астероид, прямолинейно движущийся по экрану."""
	SMALL = 1
	MEDIUM = 2
	LARGE = 3
	images = {SMALL : games.load_image("asteroid_small.bmp"),
			  MEDIUM : games.load_image("asteroid_med.bmp"),
			  LARGE : games.load_image("asteroid_big.bmp")}
	SPEED = 2
	SPAWN = 2

	def __init__(self, x, y, size):
		""" Инициализирует спрайт с изображением астероида. """
		super(Asteroid, self).__init__(
			   image = Asteroid.images[size],
			   x = x, y = y,
			   dx = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
			   dy = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size)
		
		self.size = size

	
	def die(self):
		""" разрушает астероид """
		# если размеры астероида крупные или средние, заменить его 
		# двумя более мелкими астероидами
		if self.size != Asteroid.SMALL:
			for i in range(Asteroid.SPAWN):
				new_asteroid = Asteroid(x = self.x,
										y = self.y,
										size = self.size - 1)
				games.screen.add(new_asteroid)
		
		super(Asteroid, self).die()

class Ship(Collider):
	""" Корабль игрока """
	image = games.load_image("ship.bmp") # загружаем картинку корабля
	sound = games.load_sound("thrust.wav")
	ROTATION_STEP = 3
	VELOSITY_STEP = .03
	MISSILE_DELAY = 25

	def __init__(self, x, y):
		""" Инициализирует спрайт с изображением космического корабля."""
		super(Ship, self).__init__(image = Ship.image, x = x, y = y)
		self.missile_wait = 0

	def update(self):
		""" Вращает корабль при нажатии клавишь со стрелками"""
		super(Ship, self).update()

		# rotate based on left and right arrow keys
		if games.keyboard.is_pressed(games.K_RIGHT):
			self.angle += Ship.ROTATION_STEP
		if games.keyboard.is_pressed(games.K_LEFT):
			self.angle -= Ship.ROTATION_STEP

		# корабль совершает рывок
		if games.keyboard.is_pressed(games.K_UP):
			Ship.sound.play()
			# изменение горизонтальной и вертикальной скорости корабля с учетом угла поворота
			angle = self.angle * math.pi / 180 # преобразование радианы
			self.dx += Ship.VELOSITY_STEP * math.sin(angle)
			self.dy += Ship.VELOSITY_STEP * -math.cos(angle)

		# если нажать Пробел, и интервал ожидания истек, выпустить ракету
		if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
			new_missile = Missile(self.x, self.y, self.angle)
			games.screen.add(new_missile)
			self.missile_wait = Ship.MISSILE_DELAY

		# если запуск следующей ракеты пока еще не разрешен, вычесть 1 из длины 
		# оставшегося интервала ожидания
		if self.missile_wait > 0:
			self.missile_wait -= 1

		
class Missile(Collider):
	"""Ракета, которую может выпустить космический корабль игрока. """
	image = games.load_image("missile.bmp")
	sound = games.load_sound("missile.wav")
	BUFFER = 40
	VELOSITY_FACTOR = 7
	LIFETIME = 40

	def __init__(self, ship_x, ship_y, ship_angle):
		"""Инициализирует спрайт с изображением ракеты. """
		Missile.sound.play()

		# преобразование в радианы
		angle = ship_angle * math.pi / 180

		# вычисление начальной позиции ракеты
		buffer_x = Missile.BUFFER * math.sin(angle)
		buffer_y = Missile.BUFFER * -math.cos(angle)
		x = ship_x + buffer_x
		y = ship_y + buffer_y

		# вычисление горизонтальной и вертикальной скорости ракеты
		dx = Missile.VELOSITY_FACTOR * math.sin(angle)
		dy = Missile.VELOSITY_FACTOR * -math.cos(angle)
		
		# создание ракеты
		super(Missile, self).__init__(image = Missile.image,
										x = x, y = y,
										dx = dx, dy = dy)
		self.lifetime = Missile.LIFETIME

	def update(self):
		"""Перемещает ракету"""
		super(Missile, self).update()

		# если "срок годности" ракеты истек, она уничтожается
		self.lifetime -= 1
		if self.lifetime == 0:
			self.destroy()

		


class Explosion(games.Animation):
	"""Анимированный взрыв. """
	sound = games.load_sound("explosion.wav")
	images = [ "explosion1.bmp",
					"explosion2.bmp",
					"explosion3.bmp",
					"explosion4.bmp",
					"explosion5.bmp",
					"explosion6.bmp",
					"explosion7.bmp",
					"explosion8.bmp",
					"explosion9.bmp",]
					
	def __init__(self, x, y):
		super(Explosion, self).__init__(images = Explosion.images,
										x = x, y = y,
										repeat_interval = 4, n_repeats = 1,
										is_collideable = False)
		Explosion.sound.play()



def main():
	# назначаем фоновую картинку
	nebula_image = games.load_image("nebula.jpg", transparent = False)
	games.screen.background = nebula_image

	# создаем корабль
	the_ship = Ship(x = games.screen.width/2,
					y = games.screen.height/2)  # создаем объект корабль
	games.screen.add(the_ship) # добавляем объект корабль на экран

	# создаем 8 астероидов
	for i in range(8):
		x = random.randrange(games.screen.width)
		y = random.randrange(games.screen.height)
		size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
		new_asteroid = Asteroid(x = x, y = y, size = size)

		games.screen.add(new_asteroid)

	games.screen.mainloop() # запускаем игровой цикл

main()
