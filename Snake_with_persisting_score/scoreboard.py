from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../../Desktop/data.txt") as file:  # relative file path, from current dir.
            self.high_score = int(file.read())
        self.ht()
        self.pu()
        self.color("White")
        self.goto(-160, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score} ", align="center",
                   font=("Arial", 18, "normal"))

    def increase(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/dumbe/Desktop/data.txt", mode="w") as file:  # Absolute file path, from root.
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
