# Piece.py
# Written by: Shasta Ramachandran
# Date: 2/5/2016
# Provides a large piece class for use with Chess.

# All Images from http://i.imgur.com/zwF4Lyn.png

from ChessGUI import *

class Piece:

	def __init__(self, color, x, y):
		"""Creates a piece with a given color string and location."""
		# Store the instance variable
		self.x = x
		self.y = y
		# Record whether the piece is living and drawn
		self.drawn = False
		self.living = True
		# Create the image name, which is blank and to be filled
		self.imageName = ""
		# Store the color
		self.color = color
		# Store the type
		self.type = ""
		self.hasMoved = False

	def drawPiece(self, chessGUI):
		"""Draws the piece on the given GUI object."""
		# Store coordinates to avoid passing self
		squareX,squareY = self.getCoordinates()[0],self.getCoordinates()[1]
		if(self.drawn == False):
			# Draw the image if it hasn't already been
			squareX,squareY = self.getCoordinates()[0],self.getCoordinates()[1]
			self.image = Image(chessGUI.getSquare([squareX,squareY]).getCenter(), self.imageName)
			chessGUI.draw(self.image)
			self.drawn = True

		# Otherwise, just change the parameters.
		else:
			# Move the piece to the current location
			desiredCenter = chessGUI.getSquare([squareX,squareY]).getCenter()
			dx = 1 * desiredCenter.getX() - self.image.getAnchor().getX()
			dy = 1 * desiredCenter.getY() - self.image.getAnchor().getY()
			self.image.move(dx,dy)

	def update(self, listOfTeamPieces, listOfEnemyPieces):
		"""Updates the piece's knowledge of the board using a team list and enemy list."""
		listOfTeamSquares = []
		# Put all the coordinates of team pieces into a list
		for piece in listOfTeamPieces:
			listOfTeamSquares.append(piece.getCoordinates())

		# Same for enemy pieces
		listOfEnemySquares = []

		for piece in listOfEnemyPieces:
			listOfEnemySquares.append(piece.getCoordinates())

		# Store the parameters as instance variables
		self.listOfTeamPieces = listOfTeamPieces
		self.listOfEnemyPieces = listOfEnemyPieces

		# Store the data to instance variables
		self.listOfTeamSquares = listOfTeamSquares
		self.listOfEnemySquares = listOfEnemySquares

	def kill(self):
		"""Kills a piece."""
		# Kill piece
		self.living = False
		# Undraw
		if(self.drawn):
			self.image.undraw()


	def getCoordinates(self):
		"""Returns the coordinates as a tuple."""
		return((self.x,self.y))

	def getX(self):
		"""Returns the x."""
		return self.x

	def getY(self):
		"""Returns the y."""
		return self.y

	def setCoordinates(self,coordinates):
		"""Sets the coordinates as a tuple."""
		self.x = coordinates[0]
		self.y = coordinates[1]

	def setX(self, x):
		"""sets x."""
		self.x = x

	def setY(self, y):
		"""sets y."""
		self.y = y

	def getType(self):
		"""Returns the type of the piece."""
		return self.type

	def move(self, coordinates):
		"""Moves a piece by setting self.hasMoved and changing the coordinates."""
		self.hasMoved = True
		self.setCoordinates(coordinates)

	def draw(self, gui):
		"""Confirms that a piece has moved and draws it in the GUI."""
		self.hasMoved = True
		self.drawPiece(gui)

	def moved(self):
		"""Determines whether or not the piece has moved."""
		return self.hasMoved
