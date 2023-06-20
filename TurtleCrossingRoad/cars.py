from turtle import *
import random as r

CAR_SHAPE = "square"
CAR_COLOR = ["violet","blue","green","yellow","orange","red"]
INC_SPPED = 1
STARTING_COR = [(400,-180),(400,-140),(400,-100),(400,-60),(400,-20),(400,20),(400,60),(400,100),(400,140),(400,180)]

class Cars:
    all_cars = []
    speed_lowerlim = 5
    speed_upperlim = 10

    def __init__(self) -> None:
        self.create_newcar()

    def create_newcar(self):
        new_car = Turtle(CAR_SHAPE)
        new_car.color(r.choice(CAR_COLOR))
        new_car.pu()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(r.choice(STARTING_COR))
        self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.bk(r.randint(self.speed_lowerlim,self.speed_upperlim))

    def inc_speed(self):
        self.speed_lowerlim+=INC_SPPED
        self.speed_upperlim+=INC_SPPED
