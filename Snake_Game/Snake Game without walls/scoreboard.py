from turtle import *

SCOREBOARD_COLOR = "white"
FONT = "Arial"
SIZE = 30
ALIGNMENT = "center"
SCORE_COORDINATES = (0,280)

class ScoreBoard(Turtle):
    score = 0
    def __init__(self):
        super().__init__()
        self.color(SCOREBOARD_COLOR)
        self.pu()
        self.hideturtle()
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(SCORE_COORDINATES)
        self.write(f"Score: {self.score}",True,align=ALIGNMENT,font=FONT)
        
    def update_score(self):
        self.score+=1
        self.print_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",True,align=ALIGNMENT,font=(FONT,SIZE,"normal"))

