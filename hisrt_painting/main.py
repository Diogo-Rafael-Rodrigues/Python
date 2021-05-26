import turtle as t
import random
from turtle import Screen
t.colormode(255)
tim = t.Turtle()
tim.speed(10)

color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
              (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
              (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221),
              (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210),
              (65, 66, 56)]


def set_place():

    tim.pu()
    tim.setx(-310)


def dot():
    for i in range(10):
        tim.dot(20, random.choice(color_list))
        tim.pu()
        tim.fd(50)


set_y = 0

for i in range(10):
    set_place()
    dot()
    set_y += 50
    tim.sety(set_y)

screen = Screen()
screen.exitonclick()
