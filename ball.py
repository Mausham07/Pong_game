from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        position = self.position()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def collide_y(self):
        self.y_move *= -1
        

    def collide_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def miss(self):
        self.x_move *= -1
        self.move_speed = 0.1

