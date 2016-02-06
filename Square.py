from graphics import *
class Square:
    def __init__(self,color,x,y):
        self.piece = 0
        l = 50
        self.graphicsSquare = Rectangle(Point(x,y),Point(x+l,y+l))
        

    def draw(self,window):
        self.graphicsSquare.draw(window)
