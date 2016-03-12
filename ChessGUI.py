# ChessGUI.py
# Written by: Shasta Ramachandran
# Date: 2/5/2016
# Creates a GUI object for use with Chess

from Square import *
from graphics import *
from Button import *

class ChessGUI:

	def __init__(self):
		"""Creates a GUI object for use with Chess, complete with Mouse, Square, and Message functionality."""

		# Determining the width and length
		self.width = 1000
		self.height = 700

		# Create the square colors
		self.darkSquareColor = "deep pink"
		self.darkSquareColorHighlighted = "RoyalBlue1"

		self.lightSquareColor = "hot pink"
		self.lightSquareColorHighlighted = "DarkSlateGray1"

		# Create the line color
		self.lineColor = "lavender"

		# Creating the graphics window
		self.window = GraphWin("Chess!!!", self.width, self.height)

		# Creating the background color
		self.background = "thistle3"

		# Filling in the background color
		self.window.setBackground(self.background)

		# Set the size of the chess board
		self.boardLength = self.height * 7 / 8

		# Creating the interaction options

		self.messageBox = Text(Point(self.width * 10 / 12, self.height * 1 / 4), "")
		self.messageBox.draw(self.window)
		self.messageBox.setFace("times roman")

		self. moveBox = Text(Point(self.width * 10 / 12, self.height * 1 / 2), "")
		self.moveBox.draw(self.window)
		self.moveBox.setFace("times roman")

		self.quitButton = Button(self.window, Point(self.width * 10 / 12, self.height * 2 / 3), 70, 40, "Quit", "CadetBlue1")
		self.resetButton = Button(self.window, Point(self.width * 10 / 12, self.height * 5 / 6), 70, 40, "New Game!", "CadetBlue1")

		self.quitButton.activate()

		# Create the squared grid
		self.listOfSquares = [[],[],[],[],[],[],[],[]]
		alpha = ["a","b","c","d","e","f","g","h"]
		numbers = ["1","2","3","4","5","6","7","8"]
		labelsX,labelsY = [],[]

		for i in range(8):
			for j in range(8):
				if(i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
					self.listOfSquares[i].append(Square(self.darkSquareColor, self.darkSquareColorHighlighted, self.lineColor, self.boardLength * i / 8 + self.width * 1 / 18, self.boardLength * j / 8 + self.height * 1/18, self.boardLength / 8))
				else:
					self.listOfSquares[i].append(Square(self.lightSquareColor, self.lightSquareColorHighlighted, self.lineColor, self.boardLength * i / 8 + self.width * 1 / 18, self.boardLength * j / 8 + self.height * 1/18, self.boardLength / 8))
				labelsY.append(Text(Point(self.width * 1 / 18 + self.boardLength + 15, self.boardLength * j / 8 + self.height * 1/18 + self.boardLength / 16), numbers[7-j]))
			labelsX.append(Text(Point(self.boardLength * i / 8 + self.width * 1 / 18 + self.boardLength / 16, self.height * 1/18 - 14), alpha[i]))

		# Draw the squares
		for squareList in self.listOfSquares:
			for square in squareList:
				square.draw(self.window)

		# Draw the labels
		for i in range(8):
			labelsX[i].draw(self.window)
			labelsY[i].draw(self.window)

		# Create the border lines
		self.borderLine1 = Line(Point(self.width * 1 / 18, self.height * 1/18), Point(self.boardLength + self.width * 1 / 18, self.height * 1/18))
		self.borderLine2 = Line(Point(self.width * 1 / 18, self.height * 1/18), Point(self.width * 1 / 18, self.boardLength + self.height * 1/18))
		self.borderLine3 = Line(Point(self.boardLength + self.width * 1 / 18, self.height * 1/18), Point(self.boardLength + self.width * 1 / 18, self.boardLength + self.height * 1/18))
		self.borderLine4 = Line(Point(self.width * 1 / 18, self.boardLength + self.height * 1/18), Point(self.boardLength + self.width * 1 / 18, self.boardLength + self.height * 1/18))

		# Draw the border lines
		self.borderLine1.draw(self.window)
		self.borderLine2.draw(self.window)
		self.borderLine3.draw(self.window)
		self.borderLine4.draw(self.window)

		# Change the color of the border lines
		self.borderLine1.setFill(self.lineColor)
		self.borderLine2.setFill(self.lineColor)
		self.borderLine3.setFill(self.lineColor)
		self.borderLine4.setFill(self.lineColor)

		# Create a list of highlighted squares to reduce lag
		self.highlightedSquares = []

	def getSquare(self, requestedSquare):
		"""Returns the square requested by the format of either[letter,number] or [number,number]. Works with Tuples too."""

		# Two branches in case the protocol is changed
		if(type(requestedSquare[0]) == int):
			return self.listOfSquares[requestedSquare[0]][requestedSquare[1]]
		else:
			# Use .index to convert letter to number
			return self.listOfSquares[["a","b","c","d","e","f","g","h","i"].index(requestedSquare[0])][requestedSquare[1] - 1]

	def getClickedSquare(self, point):
		"""Returns the the square at the given point, or returns false."""

		# Set a default return value		
		returnValue = False

		# Cycle through all squares to find the clicked square
		for squareList in self.listOfSquares:
			for square in squareList:
				if square.clicked(point):
					returnValue = square

		return returnValue

	def getInput(self):
		"""Validates input, waiting until a square is clicked or the quitButton is quit and returning the selected square or a QuitError."""
		while True:
			clickPoint = self.window.getMouse()
			# Test the point
			if(self.getClickedSquare(clickPoint)):
				squareToReturn = self.getClickedSquare(clickPoint)
				return(self.getIndex(squareToReturn))
				break
			elif(self.quitButton.clicked(clickPoint)):
				raise NotImplementedError("Quit by user.")

	def getIndex(self, square):
		"""Gets the X and Y of a given squarem, or returns to False, False for an error."""
		# Scan all squares to check for a match
		x = False
		y = False
		for i in range(8):
			for j in range(8):
				if(self.listOfSquares[i][j] == square):
					x = i
					y = j
		# Format the return
		tupleToReturn = (x,y)
		return(tupleToReturn)

	def getMouse(self):
		"""Gets a mouse in the window and returns the given point."""
		mouseClick = self.window.getMouse()
		return(mouseClick)

	def printMessage(self, Message):
		"""Prints a message on screen."""
		# Make sure the message ends in a period
		if(Message[-1] != "." and Message[-1] != "!"):
			Message += "."
		self.messageBox.setText(Message)

	def draw(self, objectToBeDrawn):
		"""Draws and object with proper encapsulation."""
		objectToBeDrawn.draw(self.window)

	def highlightSelectedSquare(self, requestedSquare):
		"""Highlights the square at a given coordinate."""
		# Add the square to highlighted squares and highlight it
		squareToHighlight = self.getSquare(requestedSquare)
		self.highlightedSquares.append(squareToHighlight)
		squareToHighlight.highlight()

	def unHighlightSelectedSquare(self, requestedSquare):
		"""Unhighlights the square at a given coordinate."""
		self.getSquare(requestedSquare).unHighlight()

	def unHighlightAllSquares(self):
		"""Unhighlights all squares."""
		# Use selected squares to reduce lag
		for square in self.highlightedSquares:
			square.unHighlight()

	def clearMessage(self):
		"""Clears the message being displayed."""
		self.messageBox.setText("")

	def printMoves(self, message):
		"""Prints the move message on screen."""
		# Add a period to the end if needed
		if(message[-1] != "."):
			message += "."
		# Print the message
		self.moveBox.setText(message)

	def clearMoves(self):
		"""Clears the move message."""
		self.moveBox.setText("")

	def closeWindow(self):
		"""Closes the window."""
		self.window.close()

	def reset(self):
		"""Resets the GUI window for a new game."""
		# Wait for the reset button to be clicked
		self.resetButton.activate()
		while True:
			clickPoint = self.window.getMouse()
			# Check input
			if(self.resetButton.clicked(clickPoint)):
				break
			elif(self.quitButton.clicked(clickPoint)):
				raise NotImplementedError("Quit by user.")

		# Unhighlight all Squares
		for squareList in self.listOfSquares:
			for square in squareList:
				square.unHighlight()

		# Reset the GUI Message
		self.messageBox.setText("New game! White goes first.")
