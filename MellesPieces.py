#File: MellesPieces.py
#Author: Daniel Melles
#Date: 2/8/16
#Pieces I'm doing
from Piece import *
from graphics import *
import pdb

class King(Piece):
    def __init__(self,color):
        x = 4
        if color == "white":
            y = 7
        else:
            y = 0

        super(King,self).__init__(color,x,y)
        
        self.imageName = color+"King.gif"
        self.type = "King"

        

    def movesCanMake(self,samePieces,enemyPieces):
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
    
    def isInCheck(self,samePieces,enemyPieces):
        for piece in enemyPieces:
            if (self.x,self.y) in piece.movesCanMake(enemyPieces,samePieces):
                return True
        return False


class Queen(Piece):
    def __init__(self,color):
        x = 3
        if color == "white":
            y = 7
        else:
            y = 0
        super(Queen,self).__init__(color,x,y)

        self.imageName = color+"Queen.gif"
        self.type = "Queen"

    def movesCanMake(self,samePieces,enemyPieces):
        if self.y <= self.x:
            upLeftWall = (self.x-self.y,0)
            downRightWall = (7,self.y+7-self.x)
        else:
            upLeftWall = (0,self.y-self.x)
            downRightWall = (self.x+7-self.y,7)

        if self.y <= 7-self.x:
            upRightWall = (0,self.y+self.x)
            downLeftWall = (self.x+self.y,0)
        else:
            upRightWall = (7,self.y-(7-self.x))
            downLeftWall = (self.x-(7-self.y),7)
        #In order of up/left, up/right,down/right,down/left aka clockwise
        maxDiagonals = [upLeftWall,upRightWall,downRightWall,downLeftWall]
        maxAxials = [(self.x,0),(7,self.y),(self.x,7),(0,self.y)]
        blockingPieces = [False,False,False,False]
        #In order of up, right, down, left
        for piece in samePieces:
            if piece != self:
                if abs(piece.getX()-self.x) == abs(piece.getY()-self.y):
                    diagonal,xDirection,yDirection = self.onWhichDiagonal(piece)
                    if abs(piece.getX()-self.x) <= abs(maxDiagonals[diagonal][0]-self.x):
                        blockingPieces[diagonal] = piece
                        maxDiagonals[diagonal] = (piece.getX()-xDirection,piece.getY()-yDirection)

                if piece.getX() == self.x:
                    if piece.getY() < self.y:
                        if abs(self.y-piece.getY()) <= abs(self.y-maxAxials[0][1]):
                            maxAxials[0] = (piece.getX(),piece.getY()+1)
                    else:
                        if abs(self.y-piece.getY()) <= abs(self.y-maxAxials[2][1]):
                            maxAxials[2] = (piece.getX(),piece.getY()-1)
                            
                if piece.getY() == self.y:
                    if piece.getX() > self.x:
                        if abs(self.x-piece.getX()) <= abs(self.x-maxAxials[1][0]):
                            maxAxials[1] = (piece.getX()-1,piece.getY())
                    else:
                        if abs(self.x-piece.getX()) <= abs(self.x-maxAxials[3][0]):
                            maxAxials[3] = (piece.getX()+1,piece.getY())                    
                    
        for piece in enemyPieces:
            diagonal,xDirection,yDirection = self.onWhichDiagonal(piece)
            if abs(piece.getX()-self.x) == abs(piece.getY()-self.y):
                if abs(piece.getX()-self.x) < maxDiagonals[diagonal][0]:
                    blockingPieces[diagonal] = piece
                    maxDiagonals[diagonal] = (piece.getX(),piece.getY())

            if piece.getX() == self.x:
                if piece.getY() < self.y:
                    if abs(self.y-piece.getY()) < abs(self.y-maxAxials[0][1]):
                        maxAxials[0] = (piece.getX(),piece.getY())
                else:
                    if abs(self.y-piece.getY()) < abs(self.y-maxAxials[2][1]):
                        maxAxials[2] = (piece.getX(),piece.getY())
                        
            if piece.getY() == self.y:
                if piece.getX() > self.x:
                    if abs(self.x-piece.getX()) < abs(self.x-maxAxials[1][0]):
                        maxAxials[1] = (piece.getX(),piece.getY())
                else:
                    if abs(self.x-piece.getX()) < abs(self.x-maxAxials[3][0]):
                        maxAxials[3] = (piece.getX(),piece.getY())

        movesCanMake = []
        #Diagonal
        diagonalIndex = 0
        for direction in [(-1,-1),(1,-1),(1,1),(-1,1)]:
            for i in range(1,abs(self.x-maxDiagonals[diagonalIndex][0])+1):
                if self.x+i*direction[0] >= 0 and self.y+i*direction[1] >= 0:
                    movesCanMake.append((self.x+i*direction[0],self.y+i*direction[1]))
            diagonalIndex += 1

        #On axes
        #Up,right,down,left
        axialIndex = 0
        for direction in [(0,-1),(1,0),(0,1),(-1,0)]:
            #If vertical direction
            if axialIndex == 0 or axialIndex == 2:
                for i in range(1,abs(self.y-maxAxials[axialIndex][1])+1):
                    
                    movesCanMake.append((self.x,self.y+i*direction[1]))
            #If horizontal direction
            else:
                for i in range(1,abs(self.x-maxAxials[axialIndex][0])+1):
                    movesCanMake.append((self.x+i*direction[0],self.y))
            axialIndex += 1
        
        return movesCanMake

    #Returns an index in maxDiagonals^
    def onWhichDiagonal(self,piece):
        if piece.getY() < self.y:
            if piece.getX() < self.x:
                return 0,-1,-1
            else:
                return 1,1,-1
        else:
            if piece.getX() > self.x:
                return 2,1,1
            else:
                return 3,-1,1

class Rook(Piece):
    def __init__(self,color,x):
        
        if color == 'white':
            y = 7
        else:
            y = 0
        super(Rook,self).__init__(color,x,y)
        self.imageName = color+"Rook.gif"
        self.type = "Rook"

    def movesCanMake(self,samePieces,enemyPieces):
        
        #In order of up, right, down, left
        maxAxials = [(self.x,0),(7,self.y),(self.x,7),(0,self.y)]
        
        for piece in samePieces:
            if piece != self:
                if piece.getX() == self.x:
                    if piece.getY() < self.y:
                        if abs(self.y-piece.getY()) <= abs(self.y-maxAxials[0][1]):
                            maxAxials[0] = (piece.getX(),piece.getY()+1)
                    else:
                        if abs(self.y-piece.getY()) <= abs(self.y-maxAxials[2][1]):
                            maxAxials[2] = (piece.getX(),piece.getY()-1)
                            
                if piece.getY() == self.y:
                    if piece.getX() > self.x:
                        if abs(self.x-piece.getX()) <= abs(self.x-maxAxials[1][0]):
                            maxAxials[1] = (piece.getX()-1,piece.getY())
                    else:
                        if abs(self.x-piece.getX()) <= abs(self.x-maxAxials[3][0]):
                            maxAxials[3] = (piece.getX()+1,piece.getY())                       
                    

        for piece in enemyPieces:
            if piece.getX() == self.x:
                if piece.getY() < self.y:
                    if abs(self.y-piece.getY()) < abs(self.y-maxAxials[0][1]):
                        maxAxials[0] = (piece.getX(),piece.getY())
                else:
                    if abs(self.y-piece.getY()) < abs(self.y-maxAxials[2][1]):
                        maxAxials[2] = (piece.getX(),piece.getY())
                        
            if piece.getY() == self.y:
                if piece.getX() > self.x:
                    if abs(self.x-piece.getX()) < abs(self.x-maxAxials[1][0]):
                        maxAxials[1] = (piece.getX(),piece.getY())
                else:
                    if abs(self.x-piece.getX()) < abs(self.x-maxAxials[3][0]):
                        maxAxials[3] = (piece.getX(),piece.getY())

        movesCanMake = []
        #On axes
        #Up,right,down,left
        axialIndex = 0
        for direction in [(0,-1),(1,0),(0,1),(-1,0)]:
            #If vertical direction
            if axialIndex == 0 or axialIndex == 2:
                for i in range(1,abs(self.y-maxAxials[axialIndex][1])+1):
                    movesCanMake.append((self.x,self.y+i*direction[1]))
            #If horizontal direction
            else:
                for i in range(1,abs(self.x-maxAxials[axialIndex][0])+1):
                    movesCanMake.append((self.x+i*direction[0],self.y))
            axialIndex += 1
        
        return movesCanMake
                        

        
