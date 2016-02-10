# Piece.py
# Written by: Shasta Ramachandran
# Date: 2/5/2016
# Provides a large piece class for use with Chess.

from ChessGUI import *

class Piece:

	def __init__(self, chessGUI, color, x, y):

		# Store the instance variable
		self.chessGUI = chessGUI()
		self.x = x
		self.y = y
		# Record whether the piece is living or drawn
		self.drawn = False

	def runTurnSingleGUITurn(self, movesCanMake):
		"""Runs a single turn for a given list of moves"""

		for move in movesCanMake:
			self.chessGUI.getSquare(move).highlight()
		self.chessGUI.getMouse()

	def drawPiece(self, imageFileName):
		self.Image = Image(self.GUI.getSquare(self.getCoordinates).getCenter(), image)
		if(self.drawn == False):
			# Draw the image if it hasn't already been
			self.ChessGUI.draw(self.Image)


	def update(self, listOfTeamPieces, listOfEnemyPieces):
		"""Updates the piece's knowledge of the board using a team list and enemy list."""
		listOfTeamSquares = []
		# Put all the coordinates of team pieces into a list
		for piece in listOfTeamPieces:
			listOfTeamSquares.append(piece.getCoordinates())

		# Same for enemy pieces
		listOfEnemySquares = []

		for piece in listOfTeamSquares:
			listOfEnemySquares.append(piece.getCoordinates())

		# Store the parameters as instance variables
		self.listOfTeamPieces = listOfTeamPieces
		self.listOfEnemyPieces = listOfEnemyPieces

		# Store the data to instance variables
		self.listOfTeamSquares = listOfTeamSquares
		self.listOfEnemySquares = listOfEnemySquares

	def killPiece(self):
		"""Kills a piece."""


	def getCoordinates(self):
		return((x,y))