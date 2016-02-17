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

        self.imageName = color+"King.gif"
        super(King,self).__init__(color,x,y)

        

    def possibleMoves(self,samePieces,enemyPieces):
        possibleMoves = []
        for i in range(-1,2):
            for j in range(-1,2):
                #Checking if move would go off board or is piece's current position
                if self.x+i > -1 and self.x+i < 8 and self.y+j > -1 and self.y+j < 8 and not (i==0 and j==0):
                    possibleMoves.append((self.x+i,self.y+j))

        for piece in samePieces:
            if (piece.getX(),piece.getY()) in possibleMoves:
                possibleMoves.remove((piece.getX(),piece.getY()))
        return possibleMoves


class Queen(Piece):
    def __init__(self,color):
        x = 4
        if color == "white":
            y = 7
        else:
            y = 0

        self.imageName = color+"Queen.gif"
        super(Queen,self).__init__(color,x,y)

        
