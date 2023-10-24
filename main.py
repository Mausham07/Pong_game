from turtle import Turtle, Screen
import time
from pong_paddle import PongPadlle
from ball import Ball
from score import Score


screen = Screen()
screen.bgcolor("#0A174E")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

right_paddle = PongPadlle((350, 0))
left_paddle = PongPadlle((-350, 0))
ball = Ball()
score = Score()


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collide_y()
    
    # Detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.collide_x()

    # Detect collison with left and right wall

    if ball.xcor() > 380:
        ball.miss()
        score.left_score()

    if ball.xcor() < - 380:
        ball.miss()
        score.right_score()
    

screen.exitonclick()