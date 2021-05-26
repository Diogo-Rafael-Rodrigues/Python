
import turtle as t
import random
from turtle import Screen
t.colormode(255)
tim = t.Turtle()
tim.shape("turtle")
tim.color("black")
tim.speed(100)
tim.pensize(0.5)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(200)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()
