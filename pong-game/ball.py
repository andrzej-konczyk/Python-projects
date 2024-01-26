from turtle import Turtle
import random

MOVEMENTS = [-10, 10]

class Ball(Turtle):

    def __init__(self):

        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = random.choice(MOVEMENTS)
        self.y_move = random.choice(MOVEMENTS)
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bance_move_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bance_move_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.y_move = random.choice(MOVEMENTS)
        self.bance_move_x()

