from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed("fastest")
        self.ball_speed = 0.1

    def move_ball(self):
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new, y_new)

    def y_bounce(self):
        self.y_move *= -1


    def x_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.8

    def change_target(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.x_move *= -1
