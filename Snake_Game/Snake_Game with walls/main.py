#Snake Game 
import turtle as t
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

WIDTH = 600
HEIGHT = 600
BG_COLOR = "black"
GAME_TITLE = "My Snake Game"

#setting screen
sc = t.Screen()
sc.setup(width=WIDTH, height=HEIGHT)
sc.bgcolor(BG_COLOR)
sc.title(GAME_TITLE)
sc.tracer(0)

#ceateing objects
snake = Snake()
food = Food()
score = ScoreBoard()
# wall = Wall()
#setting controls to move snake
sc.listen()
sc.onkey(snake.turn_up,"Up")
sc.onkey(snake.turn_down,"Down")
sc.onkey(snake.turn_left,"Left")
sc.onkey(snake.turn_right,"Right")

#Game starts here...
is_Game_on = True
while is_Game_on:
    sc.update()
    time.sleep(0.2)
    snake.move()
    # collision with food
    if snake.head.distance(food) <10:
        snake.grow()
        score.update_score()
        food.change_foodlocation()

    #Detect wall collision
    if snake.head.xcor()<-280 or snake.head.xcor()>280 or snake.head.ycor()<-280 or snake.head.ycor()>280:
        is_Game_on = False
        score.game_over()

    #Detect collision with tail
    if snake.tail_collision():
        is_Game_on = False
        score.game_over()

sc.exitonclick()