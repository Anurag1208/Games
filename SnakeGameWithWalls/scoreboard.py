from turtle import *

SCOREBOARD_COLOR = "white"
FONT = "Arial"
ALIGNMENT = "center"
SCORE_COORDINATES = (0,260)

class ScoreBoard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.color(SCOREBOARD_COLOR)
        self.pu()
        self.hideturtle()
        self.goto(SCORE_COORDINATES)
        self.write(f"Score: {self.score}",True,align=ALIGNMENT,font=FONT)

    def print_score(self):
        self.reset()
        self.__init__()
        
    def update_score(self):
        self.score+=1
        self.print_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",True,align=ALIGNMENT,font=FONT)
