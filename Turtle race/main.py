import random
from turtle import Turtle, Screen
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color")
colors = ["red", "Orange", "yellow", "green", "blue", "purple"]

y = 140
y_line = 160
all_turtles = []
all_lines = []
for color in colors:
    new_turtle = Turtle(shape="turtle")
    color_from_list = color
    new_turtle.color(color_from_list)
    new_turtle.pu()
    y_line -= 40
    new_turtle.goto(-230, y_line)
    all_turtles.append(new_turtle)

for color in colors:
    new_line = Turtle()
    color_from_list = color
    new_line.color(color_from_list)
    new_line.pu()
    y -= 40
    new_line.goto(-230, y)
    all_lines.append(new_line)
    new_line.pendown()
    new_line.setx(270)


if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print("Congratulations You win")
            else:
                print(f"Sorry You Lose, the {winning_color} won")

        move_forward = random.randint(0, 10)

        turtle.forward(move_forward)

screen.exitonclick()
