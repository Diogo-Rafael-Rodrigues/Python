from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong The Game")
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    # Detect Collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce()
    # Detect Collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.hit_paddle()
    # Detect Points
    if ball.xcor() == 400:
        score.increase_p1()
        ball.reset_position()

    if ball.xcor() == -400:
        score.increase_p2()
        ball.reset_position()

    if score.score_p1 == 5 or score.score_p2 == 5:
        score.game_over()
        game_is_on = False


screen.exitonclick()
