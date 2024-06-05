from turtle import Turtle, Screen


class Paddlers(Turtle):
    def __init__(self, position):
        super().__init__()
        """setting up element on screen"""
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        """xcor/ycor represents the current position of element"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """xcor/ycor represents the current position of element"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
