#File: MellesPieces.py
#Author: Daniel Melles
#Date: 2/8/16
#Pieces I'm doing
import Piece

class King(Piece):
    def __init__(self,color):
        x = 3
        if color == "white":
            y = 7
        else:
            y = 0
        super(King,self).__init__(color,x,y)
        
