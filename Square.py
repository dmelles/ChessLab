#File: Square.py
#Author: Daniel Melles
#Date: 2/8/16
#Square class

from graphics import *
class Square:
    def __init__(self,color,highlightColor,x,y,length):
        self.piece = 0
        self.length = length
        self.graphicsSquare = Rectangle(Point(x,y),Point(x+self.length,y+self.length))
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
    def getLength(self):
        return self.length
