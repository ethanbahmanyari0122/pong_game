from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")

screen.tracer(0)
paddle = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scoreboard_l = ScoreBoard((350, 260))
scoreboard_r = ScoreBoard((-350, 260))
screen.listen()

screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")
game_is_on = True

while game_is_on:
    time.sleep(0.2)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle) < 50 and ball.xcor() > 320 or \
            ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard_r.score_update()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard_l.score_update()
screen.exitonclick()
