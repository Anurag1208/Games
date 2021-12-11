from turtle import *

PADDLE_SHAPE = "square"
PADDLE_COLOR = "white"
MOVING_DIST = 20

class Paddle(Turtle):
    
    def __init__(self, x, y) -> None:
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.pu()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x,y)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + MOVING_DIST)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - MOVING_DIST)