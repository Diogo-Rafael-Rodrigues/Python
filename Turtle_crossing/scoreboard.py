from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.pu()
        self.color("Black")
        self.goto(-220, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score {self.score} ", align="center", font=FONT)

    def increase(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!!\n  Your score: {self.score}", align="center", font=("Arial", 30, "normal"))