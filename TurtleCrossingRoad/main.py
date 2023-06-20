from turtle import *
from TurtleCrossingRoad.cars import *
from TurtleCrossingRoad.tortoise import *
from TurtleCrossingRoad.scoreboard import *
import time

#constants
BG_COLOR = "black"
LINES_COLOR = "white"
DIST_FOR_COLLISION = 10
LEFTMOST_COR = [(-400,-200),(-400,-160),(-400,-120),(-400,-80),(-400,-40),(-400,0),(-400,40),(-400,80),(-400,120),(-400,160),(-400,200)]
RIGHTMOST_COR = [(400,-200),(400,-160),(400,-120),(400,-80),(400,-40),(400,0),(400,40),(400,80),(400,120),(400,160),(400,200)]
WIDTH = 800
HEIGHT = 600


class TurtleCrossingRoad():
    def setUp(self, sc) -> None:
        #screen set-up
        sc.clearscreen()
        sc.title("CROSSING ROAD GAME")
        sc.bgcolor(BG_COLOR)
        sc.setup(width=WIDTH, height=HEIGHT)
        sc.tracer(0)
        self.line = Turtle()
        self.line.hideturtle()
        self.line.color(LINES_COLOR)
        for i in range(len(LEFTMOST_COR)):
            self.line.pu()
            self.line.goto(LEFTMOST_COR[i])
            self.line.pd()
            self.line.goto(RIGHTMOST_COR[i])
        # sc.update()

        #create objects
        self.tim = Tortoise()
        self.cars = Cars()
        self.level = ScoreBoard()

        # to control turtle 
        sc.listen()
        sc.onkey(self.tim.move,"w")
        sc.onkey(self.tim.move,"Up")
        sc.onkey(self.tim.moveBack,"s")
        sc.onkey(self.tim.moveBack,"Down")

    def gameOn(self, sc):
        self.game_on = True
        self.count = 0
        while self.game_on:
            sc.update()
            time.sleep(0.1)
            self.count+=1
            if self.count%5==0:
                self.cars.create_newcar()
            self.cars.move_car()

            #level complete...
            if self.tim.ycor()>=HEIGHT/2:
                time.sleep(1)
                self.level.level_up()
                self.cars.inc_speed()
                self.tim.reset_turtle()

            #Detect Collision with cars...
            for car in self.cars.all_cars:
                if self.tim.distance(car)<=DIST_FOR_COLLISION:
                    self.game_on = False
                    self.level.game_over()
