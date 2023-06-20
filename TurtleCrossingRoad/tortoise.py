from turtle import *

COLOR = "white"
INITIAL_XCOR = 0
INITIAL_YCOR = -280
MOVE_DIST = 20

class Tortoise(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color(COLOR)
        self.shape("turtle")
        self.pu()
        self.goto(INITIAL_XCOR,INITIAL_YCOR)
        self.seth(90)

    def move(self):
        self.goto(self.xcor(),self.ycor()+MOVE_DIST)

    def moveBack(self):
        self.goto(self.xcor(),self.ycor()-MOVE_DIST)

    def reset_turtle(self):
        self.reset()
        self.__init__()
