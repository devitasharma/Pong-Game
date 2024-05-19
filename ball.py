from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_original = 10
        self.y_original = 10
        self.ball_speed = 0.1



    def move(self):
        x = self.xcor() + self.x_original

        y = self.ycor() + self.y_original
        # print(f"(x,y)={self.xcor()}{self.ycor()}")
        # print(f"y_original{self.y_original}")
        self.goto(x, y)
        # print(f" ball at {self.xcor()} and {self.ycor()}")

    def bounce_y(self):
        self.y_original *= -1


    def bounce_x(self):
        self.x_original *= -1
        self.ball_speed *= 0.9
        print(self.ball_speed)

    def reset_position(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.bounce_x()

        print(self.ball_speed)




