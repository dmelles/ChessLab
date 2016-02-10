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
        self.x = x
        self.y = y
        

    def draw(self,window):
        self.graphicsSquare.draw(window)

    def highlight(self):
        self.graphicsSquare.setFill(self.highlightColor)
    def unHighlight(self):
        self.graphicsSquare.setFill(self.color)
    def getLength(self):
        return self.length

    def clicked(self,point):
        x = point.getX()
        y = point.getY()
        p1x = self.x
        p2x = self.x+self.length
        p1y = self.y
        p2y = self.y+self.length

        #Checking if clicked point is inside square
        if (x >= p1x and x <= p2x) or (x >= p2x and x <=p1x):
            if (y >= p1y and y <= p2y) or (y >= p2y and y <=p1y):
                return True
            else:
                return False
        else:
            return False

    def getCenter(self):
        return (self.x+self.length/2,self.y+self.length/2)

