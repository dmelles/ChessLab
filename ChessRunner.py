#File: ChessRunner.py
#Author: Daniel Melles
#Date: 2/8/16
#Main logic for chess game
from ChessGUI import *
from MellesPieces import *
from RamachandranPieces import *

class ChessRunner:

    def __init__(self):
        self.gui = ChessGUI()
        self.createPieces()
        self.checkmate = False
    def runTurn(self):
        pass

    def reset(self):
        #Resets pieces lists
        self.gui.reset()
        for piece in self.whitePieces+self.blackPieces:
            piece.kill()
            
        self.createPieces()
        for piece in self.whitePieces+self.blackPieces:
            piece.drawPiece(self.gui)
        self.checkmate = False
        self.currentTeam = self.whitePieces
        
        
    
    def main(self):
        
        for piece in self.whitePieces+self.blackPieces:
            piece.drawPiece(self.gui)

        self.currentTeam = self.whitePieces

        whiteInCheck = False
        blackInCheck = False
        
        while True:
            if self.checkmate:
                self.reset()
            else:
                if self.currentTeam == self.whitePieces:
                    if not whiteInCheck:
                       self.gui.printMessage("White's turn")
                    self.otherTeam = self.blackPieces
                else:
                    if not blackInCheck:
                        self.gui.printMessage("Black's turn")
                    self.otherTeam = self.whitePieces
                hasMoved = False
            
                while not hasMoved:
                    square = self.gui.getInput()
                    if self.pieceOnSquare(self.currentTeam,square):
                        piece = self.pieceOnSquare(self.currentTeam,square)
                        for move in self.movesCanMakeWithCheck(piece):
                            self.gui.highlightSelectedSquare(move)
                        square = self.gui.getInput()
                        if square in self.movesCanMakeWithCheck(piece):

                            piecesInvolvedInMove = [piece]
                            
                            isCastleMove = False
                            if piece.getType() == 'King':
                                if square in piece.castleMoves(self.currentTeam,self.otherTeam):
                                    isCastleMove = True
                                    if square[0] < piece.getX():
                                        leftRook = piece.getRookLeft(self.currentTeam)
                                        leftRook.setCoordinates((3,leftRook.getY()))
                                        leftRook.draw(self.gui)
                                        piecesInvolvedInMove.append(leftRook)
                                    else:
                                        rightRook = piece.getRookRight(self.currentTeam)
                                        rightRook.setCoordinates((5,rightRook.getY()))
                                        rightRook.draw(self.gui)
                                        piecesInvolvedInMove.append(rightRook)
                            
                            piece.setCoordinates(square)
                            hasMoved = True
                            piece.draw(self.gui)

                            self.gui.unHighlightAllSquares()
                            pieceToRemove = False
                            
                            for otherPiece in self.otherTeam:
                                if piece.getCoordinates() == otherPiece.getCoordinates():
                                    pieceToRemove = otherPiece
                                    
                            
                            if pieceToRemove and hasMoved:
                                self.otherTeam.remove(pieceToRemove)
                                pieceToRemove.kill()
                                piecesInvolvedInMove.append(pieceToRemove)
                            self.printMoveMessage(piecesInvolvedInMove,isCastleMove)
                            self.checkForPawnToQueen(piece)
                        else:
                            self.gui.unHighlightAllSquares()
                    else:
                        self.gui.unHighlightAllSquares()
                    king = self.otherTeam[0]
                    if king.isInCheck(self.otherTeam,self.currentTeam):
                        teamString = self.getOtherTeamString()
                        if self.otherTeamIsInCheckmate():
                            self.gui.printMessage("Checkmate! {0} loses".format(teamString))
                            self.checkmate = True
                        else:
                            if teamString == 'White':
                                whiteInCheck = True
                            else:
                                blackInCheck = True
                            self.gui.printMessage(teamString+' king is in check.')
                    else:
                        whiteInCheck = False
                        blackInCheck = False
                if self.currentTeam == self.whitePieces:
                    self.currentTeam = self.blackPieces
                else:
                    self.currentTeam = self.whitePieces

    def checkForPawnToQueen(self,piece):
        
        if self.currentTeam == self.whitePieces:
            if piece.getY() == 0 and piece.getType() == 'Pawn':
                queen = Queen('white')
                queen.setCoordinates(piece.getCoordinates())
                queen.draw(self.gui)
                self.currentTeam.append(queen)
                piece.kill()
                self.currentTeam.remove(piece)
        else:
            if piece.getY() == 7 and piece.getType() == 'Pawn':
                queen = Queen('black')
                queen.setCoordinates(piece.getCoordinates())
                queen.draw(self.gui)
                self.currentTeam.append(queen)
                piece.kill()
                self.currentTeam.remove(piece)
    

    def otherTeamIsInCheckmate(self):
        king = self.otherTeam[0]
        #This method is not efficient but it is thorough
        totalMoves = []
        for piece in self.otherTeam:
            for move in piece.movesCanMake(self.otherTeam,self.currentTeam):
                previousCoordinates = piece.getCoordinates()
                piece.setCoordinates(move)
                pieceToRemove = False
                #Simulating if move would take piece
                for currentTeamPiece in self.currentTeam:
                    if piece.getCoordinates() == currentTeamPiece.getCoordinates():
                        pieceToRemove = currentTeamPiece
                if pieceToRemove:
                    currentTeamClone = []
                    for currentTeamPiece in self.currentTeam:
                        if currentTeamPiece != pieceToRemove:
                            currentTeamClone.append(currentTeamPiece)
                else:
                    currentTeamClone = self.currentTeam
                if not king.isInCheck(self.otherTeam,currentTeamClone):
                    piece.setCoordinates(previousCoordinates)
                    return False
                piece.setCoordinates(previousCoordinates)
        return True


    def movesCanMakeWithCheck(self,piece):
        #Putting this in ChessRunner because otherwise we would have to modify all the current movesCanMake methods
        movesCanMakeWithCheck = []
        movesCanMake = piece.movesCanMake(self.currentTeam,self.otherTeam)
        if piece.getType() == 'King':
            movesCanMake += piece.castleMoves(self.currentTeam,self.otherTeam)
            
        for move in movesCanMake:
            previousCoordinates = piece.getCoordinates()
            piece.setCoordinates(move)

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

            #If move wouldn't put king in check, it's a valid move            
            if not king.isInCheck(self.currentTeam,otherTeamClone):
                movesCanMakeWithCheck.append(move)
            piece.setCoordinates(previousCoordinates)
        return movesCanMakeWithCheck
                

            
        
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

    def getTeamString(self):
        if self.currentTeam == self.whitePieces:
            return 'White'
        else:
            return 'Black'
        
    def getOtherTeamString(self):
        if self.otherTeam == self.whitePieces:
            return 'White'
        else:
            return 'Black'
    
    def printMoveMessage(self,piecesInvolvedInMove,isCastleMove):
        #To map number coordinates to chess coordinates
        yCoordinates = ['8','7','6','5','4','3','2','1']
        xCoordinates = ['a','b','c','d','e','f','g','h']

        pieceThatMoved = piecesInvolvedInMove[0]

        if isCastleMove:
            message = self.getTeamString()+" castled "
            if piecesInvolvedInMove[1] == pieceThatMoved.getRookLeft(self.currentTeam):
                message += "queenside"
            else:
                message += "kingside"
        else:
            message = self.getTeamString()+" "+pieceThatMoved.getType().lower()+" moved to " +\
                      xCoordinates[pieceThatMoved.getX()]+yCoordinates[pieceThatMoved.getY()]
            if len(piecesInvolvedInMove) > 1:
                pieceTaken = piecesInvolvedInMove[1]
                message += " and took "+self.getOtherTeamString().lower()+" "+pieceTaken.getType().lower()
        self.gui.printMoves(message)
        #If piece was taken
        
        

        

runner = ChessRunner()
try:
    runner.main()
except NotImplementedError:
    #Quit logic
    runner.closeWindow()
