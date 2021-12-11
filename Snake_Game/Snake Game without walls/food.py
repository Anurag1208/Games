from turtle import *
from random import *

MIN_RANGE = -14
MAX_RANGE = 14
FOOD_COLOR = "red"
FOOD_SHAPE = "circle"

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        x = randint(MIN_RANGE,MAX_RANGE)*20
        y = randint(MIN_RANGE,MAX_RANGE)*20
        self.goto(x,y)

    def change_foodlocation(self):
        x = randint(MIN_RANGE,MAX_RANGE)*20
        y = randint(MIN_RANGE,MAX_RANGE)*20
        self.goto(x,y)

