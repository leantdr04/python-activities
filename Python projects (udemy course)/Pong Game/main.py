from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

RIGHT_PADDLE_PLACEMENT = (350, 0)
LEFT_PADDLE_PLACEMENT = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

scoreboard = Scoreboard()
r_paddle = Paddle(RIGHT_PADDLE_PLACEMENT)
l_paddle = Paddle(LEFT_PADDLE_PLACEMENT)
pong = Ball()

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_on = True
while game_on:
    time.sleep(pong.acceleration)
    screen.update()
    pong.move()

    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.wall_bounce()

    if pong.distance(r_paddle) < 50 and pong.xcor() > 330 or pong.distance(l_paddle) < 50 and pong.xcor() < -330:
        pong.paddle_bounce()

    if pong.xcor() > 390:  #Right missed, left paddle scores
        scoreboard.left_scored()
        pong.refresh()

    if pong.xcor() < -390:  #Left missed, right paddle scores
        scoreboard.right_scored()
        pong.refresh()

screen.exitonclick()
