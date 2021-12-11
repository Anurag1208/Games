from turtle import *
from time import *
from paddle import Paddle
from ball import Ball
from scoreboard import *

BGCOLOR = "Black"
TITLE = "MY Pong GAME"

#screen set-up
sc = Screen()
sc.setup(width=800,height=600)
sc.bgcolor(BGCOLOR)
sc.title(TITLE)
sc.tracer(0)

#center game line
line = Turtle()
line.color("white")
line.hideturtle()
line.pensize(10)
line.rt(90)
line.fd(400)
line.bk(800)

#objects created
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
score = ScoreBoard()
sc.update()

#keys to control paddle
sc.listen()
sc.onkey(r_paddle.move_up,"Up")
sc.onkeypress(r_paddle.move_up,"Up")
sc.onkey(l_paddle.move_up,"w")
sc.onkeypress(l_paddle.move_up,"w")
sc.onkey(r_paddle.move_down,"Down")
sc.onkeypress(r_paddle.move_down,"Down")
sc.onkey(l_paddle.move_down,"s")
sc.onkeypress(l_paddle.move_down,"s")

game_is_on = True
while game_is_on:
    sc.update()
    sleep(0.1)
    ball.move()

    #ball bouncing from wall
    if ball.ycor()==300 or ball.ycor()==-300:
        ball.bounce()

    #ball hitting right paddle
    if ball.xcor()==r_paddle.xcor()-10 and abs(ball.ycor()-r_paddle.ycor())<50:
        ball.paddle_bounce()
        ball.inc_speed()

    #ball hitting left paddle
    if ball.xcor()==l_paddle.xcor()+10 and abs(ball.ycor()-l_paddle.ycor())<50:
        ball.paddle_bounce()
        ball.inc_speed()

    #right missed
    if ball.xcor()>380:
        score.update_lscore()
        ball.reset_ball()
        sleep(1)

    #left missed
    if ball.xcor()<-380:
        score.update_rscore()
        ball.reset_ball()
        sleep(1)

    #left won
    if score.l_score==5:
        game_is_on = False
        score.game_over("Left")

    #right won
    if score.r_score==5:
        game_is_on = False
        score.game_over("Right")

sc.exitonclick()
