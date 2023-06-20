#Snake Game 
from turtle import *
from SnakeGameWithoutWalls.snake import Snake
from SnakeGameWithoutWalls.food import Food
from SnakeGameWithoutWalls.scoreboard import ScoreBoard
import time

#constants...
WIDTH = 600
HEIGHT = 600
BG_COLOR = "black"
GAME_TITLE = "My Snake Game"

class SnakeGameWithoutWalls():
    def setUp(self, sc):
        #setting screen
        sc.clearscreen()
        sc.setup(width=WIDTH, height=HEIGHT)
        sc.bgcolor(BG_COLOR)
        sc.title(GAME_TITLE)
        sc.tracer(0)

        #ceateing objects
        self.snake = Snake()
        self.food = Food()
        self.score = ScoreBoard()

        #setting controls to move snake
        sc.listen()
        sc.onkey(self.snake.turn_up,"Up")
        sc.onkey(self.snake.turn_down,"Down")
        sc.onkey(self.snake.turn_left,"Left")
        sc.onkey(self.snake.turn_right,"Right")

    def gameOn(self, sc):
        #Game starts here...
        self.is_Game_on = True
        while self.is_Game_on:
            sc.update()
            time.sleep(0.2)
            self.snake.move()
            # collision with food
            if self.snake.head.distance(self.food) <10:
                self.snake.grow()
                self.score.update_score()
                self.food.change_foodlocation()

            if self.snake.head.xcor()>300:
                self.snake.x_max()

            if self.snake.head.xcor()<-300:
                self.snake.x_min()

            if self.snake.head.ycor()>300:
                self.snake.y_max()

            if self.snake.head.ycor()<-300:
                self.snake.y_min()

            #Detect collision with tail
            if self.snake.tail_collision():
                self.is_Game_on = False
                self.score.game_over()
