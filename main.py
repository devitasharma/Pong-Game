from turtle import Turtle, Screen
from Paddlers import Paddlers
from ball import Ball
from Score_board import Score
import time

#todo setting up screen for our game
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
"""trace- to turn off screen animation"""
screen.tracer(0)

#todo creating 2 paddler obj for paddler class
right_paddle = Paddlers((350, 0))
left_paddle = Paddlers((-350, 0))
#todo creating object for ball class & scoreboard class
ball = Ball()
scoreboard = Score()

#todo run screen on click of keys
"""in to let the screen run according to your commands through keys we use .listen"""
screen.listen()
"""onKey tell which thing to perform when press particular key """
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, key="a")
screen.onkey(left_paddle.go_down, key="z")

#todo useing while loop to let the game run until false condition meets up
game_on = True
while game_on:
    """time module will delay the animation by mentioned time in between each update"""
    time.sleep(ball.ball_speed)
    """manually updating the screen as we turned off animation"""
    screen.update()
    ball.ball_movement()
    #todo ball collision check with upper and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #todo ball collision with paddle
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()
    # todo detect if right paddle missed the ball
    if ball.xcor() > 370:
       ball.reset()
       scoreboard.left_point()
    # todo detect if left paddle missed the ball
    if ball.xcor() < -370:
       ball.reset()
       scoreboard.right_point()

screen.exitonclick()
