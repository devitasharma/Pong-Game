import time
import turtle
from turtle import Turtle , Screen
from Paddlers import Paddler
from ball import Ball
import time
from Score_boad import ScoreBoard


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My First Pong Game")
screen.tracer(False)

r_paddle = Paddler((350, 0))
l_paddle = Paddler((-350, 0))
score_boad = ScoreBoard()
ball = Ball()


screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="Left")
screen.onkey(fun=l_paddle.down, key="Right")


is_game_on = True
while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()


    #Detect collision with uper and down wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:

        ball.bounce_x()


    if ball.xcor() > 380:
       ball.reset_position()
       score_boad.left_score()

    if ball.xcor() < -380:
       ball.reset_position()
       score_boad.right_score()












screen.exitonclick()