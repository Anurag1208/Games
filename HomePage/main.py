from turtle import *

#constants
SCOREBOARD_COLOR = "White"
FONT = "Courier"
SIZE = 20
HEAD_ALIGNMENT = "center"
ALIGNMENT = "left"
WIDTH = 600
HEIGHT = 600
TITLE = "GAME MANIA"
BGCOLOR = "Black"

class HomePage(Turtle):
    def setUp(self, sc) -> None:
        super().__init__()
        sc.clearscreen()
        sc.setup(width=WIDTH, height=HEIGHT)
        sc.title(TITLE)
        sc.bgcolor(BGCOLOR)
        sc.tracer(0)
        self.color(SCOREBOARD_COLOR)
        self.pu()
        self.hideturtle()
        self.printHeading()
        self.PongGame()
        self.SnakeGameWithoutWalls()
        self.SnakeGameWithWalls()
        self.CrossingRoad()
        sc.update()

    def printHeading(self):
        self.clear()
        self.goto(0,260)
        self.write("Click on the game you want to play",align=HEAD_ALIGNMENT,font=(FONT,SIZE,"normal"))
    
    def PongGame(self):
        self.goto(-200,200)
        self.write("1. Pong Game",align=ALIGNMENT,font=(FONT,SIZE,"normal"))
    
    def SnakeGameWithoutWalls(self):
        self.goto(-200,160)
        self.write("2. SnakeGameWithoutWalls",align=ALIGNMENT,font=(FONT,SIZE,"normal"))

    def SnakeGameWithWalls(self):
        self.goto(-200,120)
        self.write("3. SnakeGameWithWalls",align=ALIGNMENT,font=(FONT,SIZE,"normal"))

    def CrossingRoad(self):
        self.goto(-200,80)
        self.write("4. CrossingRoad",align=ALIGNMENT,font=(FONT,SIZE,"normal")) 
