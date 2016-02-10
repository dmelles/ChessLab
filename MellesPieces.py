#File: MellesPieces.py
#Author: Daniel Melles
#Date: 2/8/16
#Pieces I'm doing
from Piece import *
from graphics import *

class King(Piece):
    def __init__(self,color):
        x = 3
        if color == "white":
            y = 7
        else:
            y = 0

        self.image = Image(color+"King")
        super(King,self).__init__(color,x,y)
        

    def draw(self,window):
        self.image.draw(window)

    def possibleMoves(self,samePieces,enemyPieces):
        possibleMoves = []
        for i in range(-1,2):
            for j in range(-1,2):
                possibleMoves.append((self.x+i,self.y+j))
        
        
