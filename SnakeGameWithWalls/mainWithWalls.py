#Snake Game 
from turtle import *
from SnakeGameWithWalls.snake import Snake
from SnakeGameWithWalls.food import Food
from SnakeGameWithWalls.scoreboard import ScoreBoard
from SnakeGameWithWalls.wall import Wall
import time

#constants...
WIDTH = 600
HEIGHT = 600
BG_COLOR = "black"
GAME_TITLE = "My Snake Game"

class SnakeGameWithWalls():
    def setUp(self,sc) -> None:
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
        self.wall = Wall()
        self.wall.make_wall()
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

            #Detect wall collision
            if self.snake.head.xcor()<-280 or self.snake.head.xcor()>280 or self.snake.head.ycor()<-280 or self.snake.head.ycor()>280:
                self.is_Game_on = False
                self.score.game_over()

            #Detect collision with tail
            if self.snake.tail_collision():
                self.is_Game_on = False
                self.score.game_over()
