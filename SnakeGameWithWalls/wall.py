from turtle import *

WALL_COLOR = "red"
X_COR = 300
Y_COR = 300
class Wall(Turtle):

    def __init__(self):
        super().__init__()
        self.color(WALL_COLOR)
        # self.hideturtle()
        self.pensize(20)
        self.pu()
        self.goto(X_COR,Y_COR)
        self.pd()
        self.make_wall()

    def make_wall(self):
        for i in range(2):
            self.rt(90)
            self.fd(600)
