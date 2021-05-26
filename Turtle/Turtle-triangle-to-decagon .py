
import heroes
import turtle as t
import random
from turtle import pendown

from turtle import Screen

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("black")
timmy_the_turtle.speed(10)
timmy_the_turtle.pensize(10)

def t_draw(num_sides, forward, angle, color):
    for _ in range(num_sides):
        timmy_the_turtle.pencolor(color)
        timmy_the_turtle.forward(forward)
        timmy_the_turtle.lt(angle)


line_color = ["red", "blue", "purple", "LawnGreen", "Magenta", "Orange", "Yellow", "Teal"]

for i in range(3, 40):
    t_draw(i, 100, 360 / i, random.choice(line_color))

screen = Screen()
screen.exitonclick()
