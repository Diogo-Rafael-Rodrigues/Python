from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.fd(10)


def move_left():
    tim.lt(10)


def move_right():
    tim.rt(10)


def move_back():
    tim.backward(10)


def clear():
    tim.reset()

screen.listen()
screen.onkeypress(key="Up", fun=move_forward)
screen.onkeypress(key="Left", fun=move_left)
screen.onkeypress(key="Right", fun=move_right)
screen.onkeypress(key="Down", fun=move_back)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()
