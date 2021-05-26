
import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)
tim.hideturtle()
tim.color("black")
tim.speed(10)
tim.pensize(10)


def t_draw(times, directions, color):
    for _ in range(times):
        tim.pencolor(color)
        tim.forward(10)
        tim.seth(directions)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color

directions = [0, 90, 180, 270]

for i in range(50):
    t_draw(i, random.choice(directions), random_color())

screen = Screen()
screen.exitonclick()
