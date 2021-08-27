from turtle import Turtle

SCORE=[0,0]

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pu()
        self.l_score=0
        self.r_score=0
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

        self.write_score()

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.write_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.write_score()


    def write_score(self):
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))