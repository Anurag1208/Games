from turtle import *

LEVEL_COLOR = "white"
FONT = "Courier"
SIZE = 20
G_SIZE = 80
ALIGNMENT = "center"
LEVEL_X = -200
LEVEL_Y = 250

class ScoreBoard(Turtle):
    level = 1

    def __init__(self) -> None:
        super().__init__()
        self.color(LEVEL_COLOR)
        self.pu()
        self.hideturtle()
        self.goto(LEVEL_X,LEVEL_Y)
        self.print_level()

    def print_level(self):
        self.clear()
        self.write(f"Level: {self.level}",align=ALIGNMENT,font=(FONT,SIZE,"normal"))

    def level_up(self):
        self.level+=1
        self.print_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=(FONT,G_SIZE,"normal"))
