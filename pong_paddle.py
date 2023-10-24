from turtle import Turtle

class PongPadlle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("#F5D042")
        self.shapesize(5, 1, 4)
        self.penup()
        self.shape("square")
        self.goto(position)

    def go_up(self):
        new_y = self.ycor()+ 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
