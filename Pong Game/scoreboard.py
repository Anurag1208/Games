from turtle import *

SCOREBOARD_COLOR = "white"
FONT = "Courier"
SIZE = 80
ALIGNMENT = "center"

class ScoreBoard(Turtle):
    l_score = 0
    r_score = 0

    def __init__(self) -> None:
        super().__init__()
        self.color(SCOREBOARD_COLOR)
        self.pu()
        self.hideturtle()
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align=ALIGNMENT,font=(FONT,SIZE,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align=ALIGNMENT,font=(FONT,SIZE,"normal"))
        
    def update_lscore(self):
        self.l_score+=1
        self.print_score()

    def update_rscore(self):
        self.r_score+=1
        self.print_score()

    def game_over(self,winner):
        self.goto(0,0)
        self.winner = winner
        self.write(f"{winner} WON",True,align=ALIGNMENT,font=(FONT,SIZE,"normal"))