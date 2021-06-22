from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
scoreboard=Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
ball = Ball()
lpaddle = Paddle((-350, 0))
rpaddle = Paddle((350, 0))


def rpaddle_up():
    new = rpaddle.ycor() + 20
    rpaddle.goto(rpaddle.xcor(), new)


def lpaddle_up():
    new = lpaddle.ycor() + 20
    lpaddle.goto(lpaddle.xcor(), new)


def rpaddle_down():
    new = rpaddle.ycor() - 20
    rpaddle.goto(rpaddle.xcor(), new)


def lpaddle_down():
    new = lpaddle.ycor() - 20
    lpaddle.goto(lpaddle.xcor(), new)


screen.listen()
screen.onkey(rpaddle_up, "Up")
screen.onkey(rpaddle_down, "Down")
screen.onkey(lpaddle_up, "w")
screen.onkey(lpaddle_down, "s")
game_is_on = True
while game_is_on:

    ball.move()

    time.sleep(ball.move_speed)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    if ball.xcor() == 390 :
        ball.reset_position()
        scoreboard.lscore()
    if ball.xcor() == -390:
        ball.reset_position()
        scoreboard.rscore()
    if ball.distance(lpaddle) < 50 and ball.xcor() < -320 or ball.distance(rpaddle) < 50 and ball.xcor() > 320:

        ball.bounce_paddle()


    screen.update()
screen.exitonclick()
