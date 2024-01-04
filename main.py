from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Score_board
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Score_board()

screen.listen()
screen.onkey(rpaddle.up, "Up")
screen.onkey(rpaddle.down, "Down")
screen.onkey(lpaddle.up, "a")
screen.onkey(lpaddle.down, "s")
is_game_on = True


while is_game_on:

    ball.move_ball()

    # detection of the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # detection of the collision with paddle
    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 and ball.xcor() < 340 or \
            ball.distance(lpaddle) < 50 and - 320 > ball.xcor() > -340:
        ball.x_bounce()

    # detection of rpaddle missed
    if ball.xcor() > 400:
        ball.change_target()
        scoreboard.lscore()
        scoreboard.update()

    # detection of rpaddle missed
    if ball.xcor() < -400:
        ball.change_target()
        scoreboard.rscore()
        scoreboard.update()
    # checking game is finished or not
    if scoreboard.l_score > 10 or scoreboard.r_score > 10:

        scoreboard.score_check()
        is_game_on = False
    screen.update()
    time.sleep(ball.ball_speed)
screen.exitonclick()
