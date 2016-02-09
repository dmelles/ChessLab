# ChessGUI.py
# Written by: Shasta Ramachandran
# Date: 2/5/2016
# Creates a GUI object for use with Chess

from Square import *
from graphics import *

class ChessGUI:

	def __init__(self):
		"""Creates a GUI object for use with Chess, complete with Mouse, Square, and Message functionality."""

		# Determining the width and length
		self.width = 800
		self.height = 600

		# Create the square colors
		self.darkSquareColor = "black"
		self.darkSquareColorHighlighted = "blue"

		self.lightSquareColor = "white"
		self.lightSquareColorHighlighted = "yellow"

		# Creating the graphics window
		self.window = GraphWin("Chess!!!", self.width, self.height)

		# Creating the background color
		self.background = "green"

		# Filling in the background color
		self.window.setBackground(self.background)

		# Set the size of the chess board
		self.boardLength = self.height * 7 / 8

		# Creating the interaction options

	#def createBoard(self):

		# Create the squared grid
		self.listOfSquares = [[],[],[],[],[],[],[],[]]

		for i in range(8):
			for j in range(8):
				if(i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
					self.listOfSquares[i].append(Square(self.darkSquareColor, self.darkSquareColorHighlighted, self.boardLength * i / 8 + self.width * 1 / 16, self.boardLength * j / 8 + self.height * 1/16, self.boardLength / 8))
				else:
					self.listOfSquares[i].append(Square(self.lightSquareColor, self.lightSquareColorHighlighted, self.boardLength * i / 8 + self.width * 1 / 16, self.boardLength * j / 8 + self.height * 1/16, self.boardLength / 8))

		# Draw the squares
		for squareList in self.listOfSquares:
			for square in squareList:
				square.draw(self.window)

		# Create the border lines
		self.borderLine1 = Line(Point(self.width * 1 / 16, self.height * 1/16), Point(self.boardLength + self.width * 1 / 16, self.height * 1/16))
		self.borderLine2 = Line(Point(self.width * 1 / 16, self.height * 1/16), Point(self.width * 1 / 16, self.boardLength + self.height * 1/16))
		self.borderLine3 = Line(Point(self.boardLength + self.width * 1 / 16, self.height * 1/16), Point(self.boardLength + self.width * 1 / 16, self.boardLength + self.height * 1/16))
		self.borderLine4 = Line(Point(self.width * 1 / 16, self.boardLength + self.height * 1/16), Point(self.boardLength + self.width * 1 / 16, self.boardLength + self.height * 1/16))

		# Draw the border lines
		self.borderLine1.draw(self.window)
		self.borderLine2.draw(self.window)
		self.borderLine3.draw(self.window)
		self.borderLine4.draw(self.window)

		# Change the color of the border lines
		self.borderLine1.setFill(self.darkSquareColor)
		self.borderLine2.setFill(self.darkSquareColor)
		self.borderLine3.setFill(self.darkSquareColor)
		self.borderLine4.setFill(self.darkSquareColor)

	def getSquare(self, requestedSquare):
		"""Returns the square requested by the format of either[letter,number] or [number,number]."""

		# Two branches in case the protocol is changed
		if(type(requestedSquare[0]) == int):
			return self.listOfSquares[requestedSquare[0]][requestedSquare[1]]
		else:
			# Use .index to convert letter to number
			return self.listOfSquares[["a","b","c","d","e","f","g","h","i"].index(requestedSquare[0])][requestedSquare[1] - 1]

	def getMouse(self):
		# Gets a mouse 
		self.window.getMouse()


#	def highlightSelectedSquare(self, requestedSquare):
		self.getSquare(requestedSquare).highlight()

bob = ChessGUI()
