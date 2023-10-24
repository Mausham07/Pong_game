from turtle import Turtle, Screen
import time
from pong_paddle import PongPadlle


screen = Screen()
screen.bgcolor("#0A174E")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

right_paddle = PongPadlle((350, 0))
left_paddle = PongPadlle((-350, 0))


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_on = True
while game_on:
    screen.update()

screen.exitonclick()