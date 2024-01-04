from turtle import Turtle



class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100,180)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def update(self):
        self.clear()

        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def  lscore(self):
        self.l_score += 1

    def rscore(self):
        self.r_score += 1

    def score_check(self):
        self.goto((0, 0))

        self.write("game over", align="center", font=("Courier", 80, "normal"))
