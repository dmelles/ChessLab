#File: ChessRunner.py
#Author: Daniel Melles
#Date: 2/8/16
#Main logic for chess game
from ChessGUI import *
from MellesPieces import *
from RamachandranPieces import *

def main():
    gui = ChessGUI()
    whitePieces = []
    king = King('white')
    king.draw(gui)
    whitePieces.append(king)
    queen = Queen('white')
    queen.draw(gui)
    whitePieces.append(queen)
    rook1 = Rook('white',0)
    rook2 = Rook('white',7)
    whitePieces.append(rook1)
    whitePieces.append(rook2)
    rook1.draw(gui)
    rook2.draw(gui)
##    knight1 = Knight('white',1,7)
##    knight2 = Knight('white',6,7)
##    knight1.draw(gui)
##    knight2.draw(gui)
    bishop1 = Bishop('white',2,7)
    bishop2 = Bishop('white',5,7)
    bishop1.draw(gui)
    bishop2.draw(gui)
    for move in rook2.movesCanMake(whitePieces,[]):
        gui.highlightSelectedSquare(move)
    
    
main()
