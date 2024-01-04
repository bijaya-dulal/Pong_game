from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.speed("fastest")

    def up(self):
        if self.ycor() < 250 :
            new_y = self.ycor() + 80
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor()  > -250:
            new_y = self.ycor() - 80
            self.goto(self.xcor(), new_y)
