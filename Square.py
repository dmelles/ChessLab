from graphics import *
class Square:
    def __init__(self,color,highlightColor,x,y):
        self.piece = 0
        l = 50
        self.graphicsSquare = Rectangle(Point(x,y),Point(x+l,y+l))
        self.graphicsSquare.setOutline(color)
        self.graphicsSquare.setFill(color)
        self.highlightColor = highlightColor
        self.color = color
        

    def draw(self,window):
        self.graphicsSquare.draw(window)

    def highlight(self):
        self.graphicsSquare.setFill(self.highlightColor)
    def unHighlight(self):
        self.graphicsSquare.setFill(self.color)
