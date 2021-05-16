from turtle import Turtle

MOVEMENT = 20

class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(pos)
        self.penup()
        self.color("white")

    def move(self):
        self.forward(MOVEMENT)

    def up(self):
        new_y = self.ycor() + MOVEMENT
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVEMENT
        self.goto(self.xcor(), new_y)
