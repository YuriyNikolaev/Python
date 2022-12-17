# filename 03_pizza_sprite.py
# Спрайт-пицца
# Демонстрирует создание спрайта
from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50) # инициализация экрана

wall_image = games.load_image("wall.jpg", transparent = False) # загрузили изображение стены в ~ wall_image
games.screen.background = wall_image # установка картинки фоном

# к предыдущему коду добавляем следующие строки
pizza_image = games.load_image("pizza.bmp")  # загрузили изображение в переменную pizza_image

pizza = games.Sprite(image = pizza_image, x = 320, y = 240) # создали спрайт с изображением пиццы

games.screen.add(pizza) # добавление спрайта на экран

games.screen.mainloop()