# filename 01_new_graphics_window.py
# Новое графическое окно
# Демонстрирует создание графического окна
from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

games.screen.mainloop()