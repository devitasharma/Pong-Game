from turtle import Turtle

class Paddler(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("yellow")
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

