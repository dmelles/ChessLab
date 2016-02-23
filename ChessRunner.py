#File: ChessRunner.py
#Author: Daniel Melles
#Date: 2/8/16
#Main logic for chess game
from ChessGUI import *
from MellesPieces import *
from RamachandranPieces import *

class ChessRunner:

    def __init__(self):
        pass
    def runTurn(self):
        pass
    
    def main(self):
        self.gui = ChessGUI()
        self.createPieces()
        for piece in self.whitePieces+self.blackPieces:
            piece.draw(self.gui)

        self.currentTeam = self.whitePieces

        while True:
            if self.currentTeam == self.whitePieces:
                self.otherTeam = self.blackPieces
            else:
                self.otherTeam = self.whitePieces
            hasMoved = False
            
            while not hasMoved:
                square = self.gui.getInput()
                if self.pieceOnSquare(self.currentTeam,square):
                    piece = self.pieceOnSquare(self.currentTeam,square)
                    for move in piece.movesCanMake(self.currentTeam,self.otherTeam):
                        self.gui.highlightSelectedSquare(move)
                    square = self.gui.getInput()
                    if square in piece.movesCanMake(self.currentTeam,self.otherTeam):
                        previousCoords = piece.getCoordinates()
                        piece.setCoordinates(square)
                        hasMoved = True
                        king = self.currentTeam[0]
                        pieceToRemove = False
                        
                        for otherPiece in self.otherTeam:
                            if piece.getCoordinates() == otherPiece.getCoordinates():
                                pieceToRemove = otherPiece
                        if pieceToRemove:
                            otherTeamClone = []
                            for otherPiece in self.otherTeam:
                                if otherPiece != pieceToRemove:
                                    otherTeamClone.append(otherPiece)
                        else:
                            otherTeamClone = self.otherTeam
                        if king.isInCheck(self.currentTeam,otherTeamClone):
                            piece.setCoordinates(previousCoords)
                            hasMoved = False
                            self.gui.printMessage("You cannot put yourself in check")
                        piece.draw(self.gui)
                        self.gui.unHighlightAllSquares()
                        
                        if pieceToRemove and hasMoved:
                            self.otherTeam.remove(pieceToRemove)
                            pieceToRemove.kill()
                    else:
                        self.gui.unHighlightAllSquares()
                else:
                    self.gui.unHighlightAllSquares()
                self.gui.printMessage("")
                king = self.otherTeam[0]
                if king.isInCheck(self.otherTeam,self.currentTeam):
                    if self.otherTeam == self.whitePieces:
                        teamString = 'White'
                    else:
                        teamString = 'Black'
                    self.gui.printMessage(teamString+' king is in check.')
                else:
                    self.gui.printMessage("")
            if self.currentTeam == self.whitePieces:
                self.currentTeam = self.blackPieces
            else:
                self.currentTeam = self.whitePieces
                    
        
    def createPieces(self):
        self.whitePieces = []
        self.whitePieces.append(King('white'))
        self.whitePieces.append(Queen('white'))
        self.whitePieces.append(Bishop('white',2,7))
        self.whitePieces.append(Bishop('white',5,7))
        self.whitePieces.append(Knight('white',1,7))
        self.whitePieces.append(Knight('white',6,7))
        self.whitePieces.append(Rook('white',0))
        self.whitePieces.append(Rook('white',7))

        self.blackPieces = []
        self.blackPieces.append(King('black'))
        self.blackPieces.append(Queen('black'))
        self.blackPieces.append(Bishop('black',2,0))
        self.blackPieces.append(Bishop('black',5,0))
        self.blackPieces.append(Knight('black',1,0))
        self.blackPieces.append(Knight('black',6,0))
        self.blackPieces.append(Rook('black',0))
        self.blackPieces.append(Rook('black',7))

        for i in range(8):
            self.whitePieces.append(Pawn('white',i,6))
            self.blackPieces.append(Pawn('black',i,1))

        
    def pieceOnSquare(self,pieces,point):
        for piece in pieces:
            if piece.getX() == point[0] and piece.getY() == point[1]:
                return piece
        return False

    def closeWindow(self):
        self.gui.closeWindow()

runner = ChessRunner()
try:
    runner.main()
except NotImplementedError:
    runner.closeWindow()
