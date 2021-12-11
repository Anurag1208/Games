from turtle import *

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVING_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
SNAKE_SHAPE = "circle"
SNAKE_COLOR = "yellow"

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
    
    def create_snake(self):
        for i in range(len(STARTING_POSITIONS)):
            self.tim = Turtle(SNAKE_SHAPE)
            self.tim.color(SNAKE_COLOR)
            self.tim.pu()
            self.tim.goto(STARTING_POSITIONS[i])
            self.snake_body.append(self.tim)
    
    def move(self):
        for seg in range(len(self.snake_body)-1,0,-1):
            x = self.snake_body[seg-1].xcor()
            y = self.snake_body[seg-1].ycor()
            self.snake_body[seg].goto(x,y)
        self.head.fd(MOVING_DIST)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        self.tim = Turtle(SNAKE_SHAPE)
        self.tim.color(SNAKE_COLOR)
        self.tim.pu()
        self.tim.goto(self.snake_body[len(self.snake_body)-1].pos())
        self.snake_body.append(self.tim)

    def tail_collision(self):
        self.chk_collision = False
        for i in self.snake_body[1:]:
            if i.pos()==self.head.pos():
                self.chk_collision = True
        return self.chk_collision


    def x_max(self):
        self.head.setx(-300)
    
    def x_min(self):
        self.head.setx(300)

    def y_max(self):
        self.head.sety(-300)

    def y_min(self):
        self.head.sety(300)