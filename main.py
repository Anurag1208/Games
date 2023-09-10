from turtle import *
from HomePage.main import *
from Pong_Game.main import PongGame
from TurtleCrossingRoad.main import TurtleCrossingRoad
from SnakeGameWithWalls.main import SnakeGameWithWalls
from SnakeGameWithoutWalls.main import SnakeGameWithoutWalls


# making objects of game...
# sc = Screen()
# homepage = HomePage()
# pongGame = PongGame()
# snakeGameWithWalls = SnakeGameWithWalls()
# snakeGameWithoutWalls = SnakeGameWithoutWalls()
# crossingRaod = TurtleCrossingRoad()


# Main fucntionality...
# fucntion binded with click...
def func(x,y):
    if x>=-200 and x<=100:
        if y<=220 and y>=200:
            pongGame.setUp(sc=sc)
            pongGame.gameOn(sc=sc)
        elif y<=180 and y>=160:
            snakeGameWithoutWalls.setUp(sc=sc)
            snakeGameWithoutWalls.gameOn(sc=sc)
        elif y<=140 and y>=120:
            snakeGameWithWalls.setUp(sc=sc)
            snakeGameWithWalls.gameOn(sc=sc)
        elif y<=100 and y>=80:
            crossingRaod.setUp(sc=sc)
            crossingRaod.gameOn(sc=sc)

sc = Screen()
homepage = HomePage()
pongGame = PongGame()
snakeGameWithWalls = SnakeGameWithWalls()
snakeGameWithoutWalls = SnakeGameWithoutWalls()
crossingRaod = TurtleCrossingRoad()
homepage.setUp(sc=sc)
sc.onclick(func, add=False)
a = input("Press Enter to exit...")
        