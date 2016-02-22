from RamachandranPieces import *

bish = Bishop("white",1,2)
knight = Knight("black",3,4)
p = Pawn("white",6,6)

bish2 = Bishop("white",6,4)
knight2 = Knight("black",7,5)
p2 = Pawn("white",1,1)

bob = ChessGUI()
bish.draw(bob)
knight.draw(bob)
p.draw(bob)
bish2.draw(bob)
knight2.draw(bob)
p2.draw(bob)
print(type(bish))
for move in bish.movesCanMake([p,bish2,p2],[knight,knight2]):
    bob.highlightSelectedSquare(move)
bob.getMouse()
bob.unHighlightAllSquares()

for move in knight.movesCanMake([knight2],[bish,bish2,p,p2]):
    bob.highlightSelectedSquare(move)

bob.getMouse()
bob.unHighlightAllSquares()

for move in p.movesCanMake([bish,bish2,p2],[knight,knight2]):
    bob.highlightSelectedSquare(move)

bob.getMouse()
bob.unHighlightAllSquares()

for move in bish2.movesCanMake([p,bish,p2],[knight,knight2]):
    bob.highlightSelectedSquare(move)
bob.getMouse()
bob.unHighlightAllSquares()

for move in knight2.movesCanMake([knight],[bish,bish2,p,p2]):
    bob.highlightSelectedSquare(move)

bob.getMouse()
bob.unHighlightAllSquares()

for move in p2.movesCanMake([bish,bish2,p],[knight,knight2]):
    bob.highlightSelectedSquare(move)

bob.getMouse()
bob.unHighlightAllSquares()
