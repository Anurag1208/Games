from turtle import *
from time import *
from Pong_Game.paddle import Paddle
from Pong_Game.ball import Ball
from Pong_Game.scoreboard import *

#constants
BGCOLOR = "Black"
TITLE = "MY Pong GAME"
WIDTH = 800
HEIGHT = 600

class PongGame():
    def setUp(self, sc):
    #screen set-up
        sc.clearscreen()
        sc.setup(width=WIDTH,height=HEIGHT)
        sc.bgcolor(BGCOLOR)
        sc.title(TITLE)
        sc.tracer(0)

        #center game line
        self.line = Turtle()
        self.line.color("white")
        self.line.hideturtle()
        self.line.pensize(10)
        self.line.rt(90)
        self.line.fd(HEIGHT/2)
        self.line.bk(HEIGHT)

        #objects created
        self.r_paddle = Paddle(350,0)
        self.l_paddle = Paddle(-350,0)
        self.ball = Ball()
        self.score = ScoreBoard()
        sc.update()

        #keys to control paddle
        sc.listen()
        sc.onkey(self.r_paddle.move_up,"Up")
        sc.onkeypress(self.r_paddle.move_up,"Up")
        sc.onkey(self.l_paddle.move_up,"w")
        sc.onkeypress(self.l_paddle.move_up,"w")
        sc.onkey(self.r_paddle.move_down,"Down")
        sc.onkeypress(self.r_paddle.move_down,"Down")
        sc.onkey(self.l_paddle.move_down,"s")
        sc.onkeypress(self.l_paddle.move_down,"s")

    def gameOn(self, sc):
        self.game_is_on = True
        while self.game_is_on:
            sc.update()
            sleep(0.1)
            self.ball.move()

            #ball bouncing from wall
            if self.ball.ycor()>=300 or self.ball.ycor()<=-300:
                self.ball.bounce()

            #ball hitting right paddle
            if self.ball.xcor()>=self.r_paddle.xcor()-10 and self.ball.xcor()<=self.r_paddle.xcor()+10 and abs(self.ball.ycor()-self.r_paddle.ycor())<50:
                self.ball.paddle_bounce()
                self.ball.inc_speed()

            #ball hitting left paddle
            if self.ball.xcor()<=self.l_paddle.xcor()+10 and self.ball.xcor()>=self.l_paddle.xcor()-10 and abs(self.ball.ycor()-self.l_paddle.ycor())<50:
                self.ball.paddle_bounce()
                self.ball.inc_speed()

            #right missed
            if self.ball.xcor()>380:
                self.score.update_lscore()
                self.ball.reset_ball()
                sleep(1)

            #left missed
            if self.ball.xcor()<-380:
                self.score.update_rscore()
                self.ball.reset_ball()
                sleep(1)

            #left won
            if self.score.l_score==5:
                self.game_is_on = False
                self.score.game_over("Left")

            #right won
            if self.score.r_score==5:
                self.game_is_on = False
                self.score.game_over("Right")