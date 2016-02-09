# Piece.py
# Written by: Shasta Ramachandran
# Date: 2/5/2016
# Provides a large piece class for use with Chess.

class Piece:

	def __init__(self, chessGUI, color, x, y):

		# Store the instance variable
		self.chessGUI = chessGUI
		self.x = x
		self.y = y

	def runTurn(self, movesCanMake):

		for move in movesCanMake:
			self.chessGUI.getSquare(move).highlight()
		self