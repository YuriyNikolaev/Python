# ссылка RUS https://python-scripts.com/creating-game-in-30-minutes#install-pygame-zero
# ссылка ENG https://new.pythonforengineers.com/blog/your-first-game-in-python-in-less-than-30-minutes/

import pgzrun  # может быть предупреждение, но код работает
import random
import math

TITLE = "Arkanoid Clone"
WIDTH = 800
HEIGHT = 500

paddle = Actor("paddleblu.png")
paddle.x = 120
paddle.y = 420

ball = Actor("ballblue.png")
ball.x = 30
ball.y = 300

ball_x_speed = 1
ball_y_speed = 1

# bar = Actor("element_blue_rectangle_glossy.png")
# bar.x = 120
# bar.y = 100

bars_list = []


def draw():
    screen.blit("background.png", (0, 0))
    paddle.draw()
    ball.draw()
    for bar in bars_list:
        bar.draw()

def place_bars(x, y, image):
    bar_x = x
    bar_y = y
    for i in range(8):
        bar = Actor(image)
        bar.x = bar_x
        bar.y = bar_y
        bar_x += 70
        bars_list.append(bar)

def update():
    global ball_x_speed, ball_y_speed
    if keyboard.left:
        paddle.x = paddle.x - 5
    if keyboard.right:
        paddle.x = paddle.x + 5
    
    update_ball()
    for bar in bars_list:
        if ball.colliderect(bar):
            bars_list.remove(bar)
            ball_y_speed *= -1
    
    if paddle.colliderect(ball):
        ball_y_speed *= -1
        # randomly move ball left or right
        rand = random.randint(0, 1)
        if rand:
            ball_x_speed *= -1


def update_ball():
    global ball_x_speed, ball_y_speed
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    if(ball.x >= WIDTH) or (ball.x <= 0):
        ball_x_speed *= -1
    if(ball.y >= HEIGHT) or (ball.y <= 0):
        ball_y_speed *= -1

coloured_box_list = ["element_blue_rectangle_glossy.png", 
                    "element_green_rectangle_glossy.png", 
                    "element_red_rectangle_glossy.png"]
x = 120
y = 100
for coloured_box in coloured_box_list:
    place_bars(x, y, coloured_box)
    y += 50

pgzrun.go()
