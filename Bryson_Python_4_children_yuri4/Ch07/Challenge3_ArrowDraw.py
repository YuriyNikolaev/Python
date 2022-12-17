# Filename ArrowDraw.py
# оказалось сложнее, чем думал. пока не работает

import turtle
t = turtle.Pen()
t.speed(0)
t.turtlesize(2, 2, 2) # увеличивает размер и контур стрелки
leanth = 50


def longer():
        leanth += 5


def shorter():
        leanth -= 5
        

def up():
        if "." :
                t.forward(longer)
        else ",":
                t.forward(shorter)

def left():
	t.left(15)
def right():
	t.right(15)
	
turtle.onkeypress(up, "Up")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(shorter, ",")
turtle.onkeypress(longer, ".")




turtle.listen() # инструкция о начале прослушивания нажатия клавиш
