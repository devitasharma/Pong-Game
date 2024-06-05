from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update()
    def update(self):
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 50, "normal"))

    def right_point(self):
        self.clear()
        self.right_score +=1
        self.update()

    def left_point(self):
        self.clear()
        self.left_score +=1
        self.update()