from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.number = 0
        self.color("white")
        self.penup()
        self.goto(pos)
        self.hideturtle()
        self.score_writing()

    def score_writing(self):
        self.write(f"Score: {self.number}", align="center", font=("Arial", 14, "normal"))

    def score_update(self):
        self.number += 1
        self.clear()
        self.score_writing()
