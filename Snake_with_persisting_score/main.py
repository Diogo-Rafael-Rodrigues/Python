import time
from snake import Snake
from food import Food
from turtle import Screen
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("Black")
screen.title("Crazy Snake")
screen.tracer(0)

snake = Snake()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")

food = Food()
score = Scoreboard()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 18:
        score.increase()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            score.reset()
            snake.reset()








screen.exitonclick()
