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
    
    def main(self):
        self.gui = ChessGUI()
        whitePieces,blackPieces = self.createPieces()
        for piece in whitePieces+blackPieces:
            piece.draw(self.gui)

        currentTeam = 'white'

        while True:
            if currentTeam == 'white':
                hasMoved = False
                while not hasMoved:
                    square = self.gui.getInput()
                    if self.pieceOnSquare(whitePieces,square):
                        piece = self.pieceOnSquare(whitePieces,square)
                        for move in piece.movesCanMake(whitePieces,blackPieces):
                            self.gui.highlightSelectedSquare(move)
                        square = self.gui.getInput()
                        if square in piece.movesCanMake(whitePieces,blackPieces):
                            piece.setCoordinates(square)
                            piece.draw(self.gui)
                            self.gui.unHighlightAllSquares()
                            pieceToRemove = False
                            for blackPiece in blackPieces:
                                if piece.getCoordinates() == blackPiece.getCoordinates():
                                    print("Killing piece")
                                    pieceToRemove = blackPiece
                                    break
                            if pieceToRemove:
                                blackPieces.remove(pieceToRemove)
                                pieceToRemove.kill()
                            hasMoved = True
                        else:
                            self.gui.unHighlightAllSquares()
                    else:
                       self.gui.unHighlightAllSquares()
                currentTeam = 'black'
            else:
                hasMoved = False
                while not hasMoved:
                    square = self.gui.getInput()
                    if self.pieceOnSquare(blackPieces,square):
                        piece = self.pieceOnSquare(blackPieces,square)
                        for move in piece.movesCanMake(blackPieces,whitePieces):
                            self.gui.highlightSelectedSquare(move)
                        square = self.gui.getInput()
                        if square in piece.movesCanMake(blackPieces,whitePieces):
                            piece.setCoordinates(square)
                            piece.draw(self.gui)
                            self.gui.unHighlightAllSquares()
                            pieceToRemove = False
                            for whitePiece in whitePieces:
                                if piece.getCoordinates() == whitePiece.getCoordinates():
                                    pieceToRemove = whitePiece
                                    break
                            if pieceToRemove:
                                whitePieces.remove(pieceToRemove)
                                pieceToRemove.kill()
                            hasMoved = True
                        else:
                            self.gui.unHighlightAllSquares()
                    else:
                       self.gui.unHighlightAllSquares()
                currentTeam = 'white'
        
                    
        
    def createPieces(self):
        whitePieces = []
        whitePieces.append(King('white'))
        whitePieces.append(Queen('white'))
        whitePieces.append(Bishop('white',2,7))
        whitePieces.append(Bishop('white',5,7))
        whitePieces.append(Knight('white',1,7))
        whitePieces.append(Knight('white',6,7))
        whitePieces.append(Rook('white',0))
        whitePieces.append(Rook('white',7))

        blackPieces = []
        blackPieces.append(King('black'))
        blackPieces.append(Queen('black'))
        blackPieces.append(Bishop('black',2,0))
        blackPieces.append(Bishop('black',5,0))
        blackPieces.append(Knight('black',1,0))
        blackPieces.append(Knight('black',6,0))
        blackPieces.append(Rook('black',0))
        blackPieces.append(Rook('black',7))

        for i in range(8):
            whitePieces.append(Pawn('white',i,6))
            blackPieces.append(Pawn('black',i,1))

        return whitePieces,blackPieces
        
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
