from turtle import *
from math import *

BALL_COLOR = "white"
BALL_SHAPE = "circle"
X_MOVE = 10
Y_MOVE = 10
INC_SPEED = 5
MAX_SPEED = 30

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.pu()
        self.x_move = X_MOVE
        self.y_move = Y_MOVE

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)

    def bounce(self):
        self.y_move*= -1

    def paddle_bounce(self):
        self.x_move*= -1

    def reset_ball(self):
        self.goto(0,0)
        self.x_move = X_MOVE*self.sgn(self.x_move)
        self.y_move = Y_MOVE*self.sgn(self.y_move)

    def inc_speed(self):
        self.x_move+= INC_SPEED*self.sgn(self.x_move)
        self.y_move+= INC_SPEED*self.sgn(self.y_move)
        self.x_move = min(self.x_move,MAX_SPEED)
        self.y_move = min(self.y_move,MAX_SPEED)

    def sgn(self,n):
        if abs(n)==n:
            return 1
        else :
            return -1
