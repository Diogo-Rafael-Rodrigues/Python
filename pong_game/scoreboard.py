from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_p1 = 0
        self.score_p2 = 0
        self.ht()
        self.pu()
        self.color("White")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f" {self.score_p1} Score {self.score_p2}  ", align="center", font=("Arial", 18, "normal"))

    def increase_p1(self):
        self.clear()
        self.score_p1 += 1
        self.update_scoreboard()

    def increase_p2(self):
        self.clear()
        self.score_p2 += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!!\n ", align="center", font=("Arial", 30, "normal"))
        if self.score_p1 > self.score_p2:
            self.write("PLAYER ONE WIN!", align="center", font=("Arial", 30, "normal"))
        else:
            self.write("PLAYER TWO WIN!", align="center", font=("Arial", 30, "normal"))
