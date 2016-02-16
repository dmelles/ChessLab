# Piece.py
# Written by: Shasta Ramachandran
# Date: 2/5/2016
# Provides a large piece class for use with Chess.

# All Images from http://i.imgur.com/zwF4Lyn.png

from ChessGUI import *

class Piece:

	def __init__(self, color, x, y):

		# Store the instance variable
		self.x = x
		self.y = y
		# Record whether the piece is living and drawn
		self.drawn = False
		self.living = True
		# Create the image name, which is blank and to be filled
		self.ImageName = ""

	def draw(self, chessGUI):
		"""Draws the piece on the given GUI object."""
		if(self.drawn == False):
			# Draw the image if it hasn't already been
			squareX,squareY = self.getCoordinates()[0],self.getCoordinates()[1]
			self.Image = Image(chessGUI.getSquare([squareX,squareY]).getCenter(), self.ImageName)
			chessGUI.draw(self.Image)
			self.drawn = True

		# Otherwise, just change the parameters.
		else:
			# Move the pieve to the current location
			dx = 1 * self.getCoordinates[0] - self.Image.getAnchor().getX()
			dy = 1 * self.getCoordinates[1] - self.Image.getAnchor().getY()
			self.Image.move(dx,dy)

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
		# Kill piece
		self.living = False
		# Undraw
		if(self.drawn):
			self.Image.undraw()


	def getCoordinates(self):
		return((self.x,self.y))

bob = ChessGUI()
p = Piece("black", 7, 7)
p.ImageName = "fish 0 d False.gif"
p.draw(bob)
