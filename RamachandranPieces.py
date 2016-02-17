# Bishop.py
# Written by: Shasta Ramachandran
# Date: 2/16/2016
# Creates all of Shasta's pieces.

from piece import *

class Bishop(Piece):
	"""Creates a bishop piece."""

	def __init__(self, color, x, y):
		"""Create a Bishop piece with the given settings"""
		super(Piece,self).__init__(color, x, y)
		# Set the filename, using self.color
		self.imageName = self.color + "Bishop.gif"

	def movesCanMake(self, teamPieces, enemyPieces):
		"""Gives the moves the bishop can make for a given board configuration."""
		# Update the piece's knowledge of the board
		self.update(teamPieces, enemyPieces)

		# Check the diagonals for places the bishop can move
		movesCanMake = []

		# Find the grid to test
		gridToTest = self.getCoordinates

		# Start by heading in the ++ diagonal
		while True:

			# Advance the tested square
			gridToTest = (gridToTest[0] + 1,gridToTest[1] + 1)

			# Make sure the piece is not out of bounds
			if(gridToTest[0] > 7 or gridToTest[1] > 7):
				break

			# See if the piece is blocked by any other piece, using a strict test for pieces of the same team and a soft test for enemy pieces

			if(gridToTest in self.listOfTeamSquares):
				break

			if(gridToTest in self.listOfEnemySquares):
				movesCanMake.append(gridToTest)
				break

			# If the loop is still unbroken, add the current piece
			movesCanMake.append(gridToTest)

		# Continue in the +- diagonal
		while True:

			# Advance the tested square
			gridToTest = (gridToTest[0] + 1,gridToTest[1] - 1)

			# Make sure the piece is not out of bounds
			if(gridToTest[0] > 7 or gridToTest[1] < 0):
				break

			# See if the piece is blocked by any other piece, using a strict test for pieces of the same team and a soft test for enemy pieces

			if(gridToTest in self.listOfTeamSquares):
				break

			if(gridToTest in self.listOfEnemySquares):
				movesCanMake.append(gridToTest)
				break

			# If the loop is still unbroken, add the current piece
			movesCanMake.append(gridToTest)

		# Continue in the -+ diagonal
		while True:

			# Advance the tested square
			gridToTest = (gridToTest[0] - 1,gridToTest[1] + 1)

			# Make sure the piece is not out of bounds
			if(gridToTest[0] < 0 or gridToTest[1] > 7):
				break

			# See if the piece is blocked by any other piece, using a strict test for pieces of the same team and a soft test for enemy pieces

			if(gridToTest in self.listOfTeamSquares):
				break

			if(gridToTest in self.listOfEnemySquares):
				movesCanMake.append(gridToTest)
				break

			# If the loop is still unbroken, add the current piece
			movesCanMake.append(gridToTest)

				# Continue in the -- diagonal
		while True:

			# Advance the tested square
			gridToTest = (gridToTest[0] - 1,gridToTest[1] - 1)

			# Make sure the piece is not out of bounds
			if(gridToTest[0] < 0 or gridToTest[1] < 0):
				break

			# See if the piece is blocked by any other piece, using a strict test for pieces of the same team and a soft test for enemy pieces

			if(gridToTest in self.listOfTeamSquares):
				break

			if(gridToTest in self.listOfEnemySquares):
				movesCanMake.append(gridToTest)
				break

			# If the loop is still unbroken, add the current piece
			movesCanMake.append(gridToTest)

		return(movesCanMake)

class Horse(Piece):
	"""Creates a bishop piece."""

	def __init__(self, color, x, y):
		"""Create a Horse piece with the given settings"""
		super(Piece,self).__init__(color, x, y)
		# Set the filename, using self.color
		self.imageName = self.color + "Horse.gif"

	def movesCanMake(self, teamPieces, enemyPieces):
		"""Gives the moves the horse can make for a given board configuration."""
		# Update the piece's knowledge of the board
		self.update(teamPieces, enemyPieces)

		# Check the diagonals for places the horse can move
		movesCanMake = []

		# Find the grid to test
		gridToTest = self.getCoordinates()

		# Directions: +3+1,+1+3,+3-1,-1+3,-3+1,+1-3,-1-3,-3-1

		# Start by heading in the +3+1 direction

		# Advance the tested square
		gridToTest = (gridToTest[0] + 3,gridToTest[1] + 1)

		# Make sure the piece is not out of bounds
		if(gridToTest[0] > 7 or gridToTest[0] < 0 or gridToTest[1] > 7 or gridToTest[1] < 0):
			# Do nothing
		else:
			# See if the piece is blocked by any other piece on the same team

			if(gridToTest in self.listOfTeamSquares):
				break
			else:
				movesCanMake.append(gridToTest)

		# Test +1+3

		# Advance the tested square
		gridToTest = self.getCoordinates()
		gridToTest = (gridToTest[0] + 1,gridToTest[1] + 3)

		# Make sure the piece is not out of bounds
		if(gridToTest[0] > 7 or gridToTest[0] < 0 or gridToTest[1] > 7 or gridToTest[1] < 0):
			# Do nothing
		else:
			# See if the piece is blocked by any other piece on the same team

			if(gridToTest in self.listOfTeamSquares):
				break
			else:
				movesCanMake.append(gridToTest)

		# Test -1+3

		# Advance the tested square
		gridToTest = self.getCoordinates()
		gridToTest = (gridToTest[0] - 1,gridToTest[1] + 3)

		# Make sure the piece is not out of bounds
		if(gridToTest[0] > 7 or gridToTest[0] < 0 or gridToTest[1] > 7 or gridToTest[1] < 0):
			# Do nothing
		else:
			# See if the piece is blocked by any other piece on the same team

			if(gridToTest in self.listOfTeamSquares):
				break
			else:
				movesCanMake.append(gridToTest)

		# Test +3-1

		# Advance the tested square
		gridToTest = self.getCoordinates()
		gridToTest = (gridToTest[0] + 3,gridToTest[1] - 1)

		# Make sure the piece is not out of bounds
		if(gridToTest[0] > 7 or gridToTest[0] < 0 or gridToTest[1] > 7 or gridToTest[1] < 0):
			# Do nothing
		else:
			# See if the piece is blocked by any other piece on the same team

			if(gridToTest in self.listOfTeamSquares):
				break
			else:
				movesCanMake.append(gridToTest)

		# Test -3+1

		# Advance the tested square
		gridToTest = self.getCoordinates()
		gridToTest = (gridToTest[0] - 3,gridToTest[1] + 1)

		# Make sure the piece is not out of bounds
		if(gridToTest[0] > 7 or gridToTest[0] < 0 or gridToTest[1] > 7 or gridToTest[1] < 0):
			# Do nothing
		else:
			# See if the piece is blocked by any other piece on the same team

			if(gridToTest in self.listOfTeamSquares):
				break
			else:
				movesCanMake.append(gridToTest)

		# Test +1-3

		# Advance the tested square
		gridToTest = self.getCoordinates()
		gridToTest = (gridToTest[0] + 1,gridToTest[1] - 3)

		# Make sure the piece is not out of bounds
		if(gridToTest[0] > 7 or gridToTest[0] < 0 or gridToTest[1] > 7 or gridToTest[1] < 0):
			# Do nothing
		else:
			# See if the piece is blocked by any other piece on the same team

			if(gridToTest in self.listOfTeamSquares):
				break
			else:
				movesCanMake.append(gridToTest)

		# Test -3-1

		# Advance the tested square
		gridToTest = (gridToTest[0] - 3,gridToTest[1] - 1)

		# Make sure the piece is not out of bounds
		if(gridToTest[0] > 7 or gridToTest[0] < 0 or gridToTest[1] > 7 or gridToTest[1] < 0):
			# Do nothing
		else:
			# See if the piece is blocked by any other piece on the same team

			if(gridToTest in self.listOfTeamSquares):
				break
			else:
				movesCanMake.append(gridToTest)

		# Test -1-3

		# Advance the tested square
		gridToTest = self.getCoordinates()
		gridToTest = (gridToTest[0] - 1,gridToTest[1] - 3)

		# Make sure the piece is not out of bounds
		if(gridToTest[0] > 7 or gridToTest[0] < 0 or gridToTest[1] > 7 or gridToTest[1] < 0):
			# Do nothing
		else:
			# See if the piece is blocked by any other piece on the same team

			if(gridToTest in self.listOfTeamSquares):
				break
			else:
				movesCanMake.append(gridToTest)
				
		return(movesCanMake)