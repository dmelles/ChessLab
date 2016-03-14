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

            
    
    def main(self):

        #Draw pieces on board
        for piece in self.whitePieces+self.blackPieces:
            #drawPiece() instead of draw() so piece.hasMoved isn't set to true
            piece.drawPiece(self.gui)
        
        self.currentTeam = self.whitePieces

        whiteInCheck = False
        blackInCheck = False

        #Loop will only exit when quit button is clicked
        while True:
            if self.checkmate:
                self.reset()
            else:
                if self.currentTeam == self.whitePieces:
                    #Check variable is solely for message purposes
                    if not whiteInCheck:
                       self.gui.printMessage("White's turn")
                    self.otherTeam = self.blackPieces
                else:
                    if not blackInCheck:
                        self.gui.printMessage("Black's turn")
                    self.otherTeam = self.whitePieces
                hasMoved = False

                #While no move has been made
                while not hasMoved:
                    #Get clicked square
                    square = self.gui.getInput()

                    #Check if there is a current team piece on the clicked square
                    if self.pieceOnSquare(self.currentTeam,square):
                        piece = self.pieceOnSquare(self.currentTeam,square)

                        #Highlight moves the piece can make without putting its king in check
                        for move in self.movesCanMakeWithCheck(piece):
                            self.gui.highlightSelectedSquare(move)
                        square = self.gui.getInput()

                        #If clicked square in  moves the piece can make without putting its king in check
                        if square in self.movesCanMakeWithCheck(piece):

                            #For printing move message
                            piecesInvolvedInMove = [piece]

                            #Castle logic
                            isCastleMove = False
                            if piece.getType() == 'King':
                                if square in piece.castleMoves(self.currentTeam,self.otherTeam):
                                    isCastleMove = True
                                   
                                    if square[0] < piece.getX():
                                         #If castling queenside
                                        leftRook = piece.getRookLeft(self.currentTeam)
                                        leftRook.setCoordinates((3,leftRook.getY()))
                                        leftRook.draw(self.gui)
                                        piecesInvolvedInMove.append(leftRook)
                                    else:
                                        #If castling kingside
                                        rightRook = piece.getRookRight(self.currentTeam)
                                        rightRook.setCoordinates((5,rightRook.getY()))
                                        rightRook.draw(self.gui)
                                        piecesInvolvedInMove.append(rightRook)

                            #Move piece
                            piece.setCoordinates(square)
                            hasMoved = True
                            piece.draw(self.gui)

                            self.gui.unHighlightAllSquares()
                            pieceToRemove = False

                            #Check if piece was taken
                            for otherPiece in self.otherTeam:
                                if piece.getCoordinates() == otherPiece.getCoordinates():
                                    pieceToRemove = otherPiece
                                    
                            #Removing piece logic
                            if pieceToRemove:
                                self.otherTeam.remove(pieceToRemove)
                                pieceToRemove.kill()
                                piecesInvolvedInMove.append(pieceToRemove)

                            #Print appropriate message to GUI
                            self.printMoveMessage(piecesInvolvedInMove,isCastleMove)
                            #Check if pawn is at the end of the board
                            self.checkForPawnToQueen(piece)
                        else:
                            #User clicked on a square that was an invalid move
                            self.gui.printMoves("Not a valid move")
                            self.gui.unHighlightAllSquares()
                    else:
                        #User didn't click on a current team piece
                        self.gui.printMoves("You must pick a "+self.getTeamString().lower()+" piece")
                        self.gui.unHighlightAllSquares()

                    #Check logic
                    king = self.otherTeam[0]
                    if king.isInCheck(self.otherTeam,self.currentTeam):
                        teamString = self.getOtherTeamString()
                        
                        #Checkmate logic
                        if self.otherTeamIsInCheckmate():
                            self.gui.printMessage("Checkmate! {0} loses".format(teamString))
                            self.checkmate = True
                        else:
                            if teamString == 'White':
                                #For message printing purposes
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
            #For a white pawn
            if piece.getY() == 0 and piece.getType() == 'Pawn':
                #Create queen at pawn's coordinates
                queen = Queen('white')
                queen.setCoordinates(piece.getCoordinates())
                queen.draw(self.gui)
                self.currentTeam.append(queen)
                #Undraw pawn and remove it from current team
                piece.kill()
                self.currentTeam.remove(piece)
        else:
            if piece.getY() == 7 and piece.getType() == 'Pawn':
                #Same logic as above but for black
                queen = Queen('black')
                queen.setCoordinates(piece.getCoordinates())
                queen.draw(self.gui)
                self.currentTeam.append(queen)
                piece.kill()
                self.currentTeam.remove(piece)
    

    def otherTeamIsInCheckmate(self):
        king = self.otherTeam[0]
        totalMoves = []
        #Checking if there are any moves the other team can make that won't put them in check
        #If not, it is checkmate
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

                #If there is a valid move, return False
                if not king.isInCheck(self.otherTeam,currentTeamClone):
                    piece.setCoordinates(previousCoordinates)
                    return False
                piece.setCoordinates(previousCoordinates)
        #If program has gotten here, it means the other team has no moves and it is checkmate
        return True


    def movesCanMakeWithCheck(self,piece):
        #Putting this in ChessRunner because otherwise we would have to modify all the current movesCanMake methods
        movesCanMakeWithCheck = []
        movesCanMake = piece.movesCanMake(self.currentTeam,self.otherTeam)

        #Adding castle moves for king
        if piece.getType() == 'King':
            movesCanMake += piece.castleMoves(self.currentTeam,self.otherTeam)

        #For each move, test if it would put the king in check
        for move in movesCanMake:
            previousCoordinates = piece.getCoordinates()
            piece.setCoordinates(move)

            king = self.currentTeam[0]
            pieceToRemove = False

            #Simulating removing a piece
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
                

    #To start new game
    def reset(self):
        #Waits for a click of the reset or quit button
        self.gui.reset()
        #Undraws pieces on the board
        for piece in self.whitePieces+self.blackPieces:
            piece.kill()

        #Resets pieces lists
        self.createPieces()

        #Draw new pieces and set initial variables
        for piece in self.whitePieces+self.blackPieces:
            piece.drawPiece(self.gui)
        self.checkmate = False
        self.currentTeam = self.whitePieces
        
           
        
    def createPieces(self):

        #Create pieces for both teams
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

        
    def pieceOnSquare(self,pieces,square):
        #Given a team, will loop through team and see if any pieces' positions are on the given square
        for piece in pieces:
            if piece.getX() == square[0] and piece.getY() == square[1]:
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
            #If piece was taken
            if len(piecesInvolvedInMove) > 1:
                pieceTaken = piecesInvolvedInMove[1]
                
                message += " and took "+self.getOtherTeamString().lower()+" "+pieceTaken.getType().lower()
        self.gui.printMoves(message)
        
        
        

        

runner = ChessRunner()
try:
    runner.main()
except NotImplementedError:
    #Quit logic
    runner.closeWindow()
