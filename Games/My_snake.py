from turtle import *
import turtle
from random import randrange
from freegames import vector, square

food = vector(0, 0)
aim = vector(0, -8)

# Todo Create Window
win = turtle.Screen()
win.setup(width=800, height=600)
win.bgcolor('black')


# Todo Create food
def create_food():
    f = turtle.Turtle()
    f.shape('square')
    f.shapesize(1)
    f.color('green')
    f.penup()
    f.sety(randrange(-12, 12) * 8)
    f.setx(randrange(-12, 12) * 8)


# Todo create Snake
snake = [vector(8, 0)]


listen()
onkey(create_food, 'Up')


# Todo Move




