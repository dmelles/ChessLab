# RamachandranPieces.py
# Written by: Shasta Ramachandran
# Date: 2/16/2016
# Creates all of Shasta's pieces.

from Piece import *

class Bishop(Piece):
	"""Creates a bishop piece."""

	def __init__(self, color, x, y):
		"""Create a Bishop piece with the given settings"""
		super(Bishop,self).__init__(color, x, y)
		# Set the filename, using self.color
		self.imageName = self.color + "Bishop.gif"
		self.type = "Bishop"

	def movesCanMake(self, teamPieces, enemyPieces):
		"""Gives the moves the bishop can make for a given board configuration."""
		# Update the piece's knowledge of the board
		self.update(teamPieces, enemyPieces)
		# Check the diagonals for places the bishop can move
		movesCanMake = []
		# Find the grid to test
		gridToTest = self.getCoordinates()

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
		# Reset grid
		gridToTest = self.getCoordinates()
		# Advance the tested square
		while True:
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
		# Reset grid
		gridToTest = self.getCoordinates()
		# Advance the tested square
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
		# Reset grid
		gridToTest = self.getCoordinates()
		# Advance the tested square
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

class Knight(Piece):
	"""Creates a Knight piece."""

	def __init__(self, color, x, y):
		"""Create a Knight piece with the given settings"""
		super(Knight,self).__init__(color, x, y)
		# Set the filename, using self.color
		self.imageName = self.color + "Knight.gif"
		self.type = "Knight"

	def movesCanMake(self, teamPieces, enemyPieces):
		"""Gives the moves the knight can make for a given board configuration."""
		# Update the piece's knowledge of the board
		self.update(teamPieces, enemyPieces)

		# Check the diagonals for places the knight can move
		movesCanMake = []

		# Find the grid to test
		gridToTest = self.getCoordinates()

		# Directions: +2+1,+1+2,+2-1,-1+2,-2+1,+1-2,-1-2,-2-1

		# Start by heading in the +2+1 direction

		# Advance the tested square
		gridToTest = (gridToTest[0] + 2,gridToTest[1] + 1)

		# Make sure the piece is not out of bounds
		if(gridToTest[0] > 7 or gridToTest[0] < 0 or gridToTest[1] > 7 or gridToTest[1] < 0):
			# Do nothing
			pass
		else:
			# See if the piece is blocked by any other piece on the same team

			if(gridToTest in self.listOfTeamSquares):
				pass
			else:
				movesCanMake.append(gridToTest)

		# Test +1+2

		# Advance the tested square
		gridToTest = self.getCoordinates()
		gridToTest = (gridToTest[0] + 1,gridToTest[1] + 2)

		# Make sure the piece is not out of bounds
		if(gridToTest[0] > 7 or gridToTest[0] < 0 or gridToTest[1] > 7 or gridToTest[1] < 0):
			# Do nothing
			pass
		else:
			# See if the piece is blocked by any other piece on the same team

			if(gridToTest in self.listOfTeamSquares):
				pass
			else:
				movesCanMake.append(gridToTest)

		# Test -1+2

		# Advance the tested square
		gridToTest = self.getCoordinates()
		gridToTest = (gridToTest[0] - 1,gridToTest[1] + 2)

		# Make sure the piece is not out of bounds
		if(gridToTest[0] > 7 or gridToTest[0] < 0 or gridToTest[1] > 7 or gridToTest[1] < 0):
			# Do nothing
			pass
		else:
			# See if the piece is blocked by any other piece on the same team

			if(gridToTest in self.listOfTeamSquares):
				pass
			else:
				movesCanMake.append(gridToTest)

		# Test +2-1

		# Advance the tested square
		gridToTest = self.getCoordinates()
		gridToTest = (gridToTest[0] + 2,gridToTest[1] - 1)

		# Make sure the piece is not out of bounds
		if(gridToTest[0] > 7 or gridToTest[0] < 0 or gridToTest[1] > 7 or gridToTest[1] < 0):
			# Do nothing
			pass
		else:
			# See if the piece is blocked by any other piece on the same team

			if(gridToTest in self.listOfTeamSquares):
				pass
			else:
				movesCanMake.append(gridToTest)

		# Test -2+1

		# Advance the tested square
		gridToTest = self.getCoordinates()
		gridToTest = (gridToTest[0] - 2,gridToTest[1] + 1)

		# Make sure the piece is not out of bounds
		if(gridToTest[0] > 7 or gridToTest[0] < 0 or gridToTest[1] > 7 or gridToTest[1] < 0):
			# Do nothing
			pass
		else:
			# See if the piece is blocked by any other piece on the same team

			if(gridToTest in self.listOfTeamSquares):
				pass
			else:
				movesCanMake.append(gridToTest)

		# Test +1-2

		# Advance the tested square
		gridToTest = self.getCoordinates()
		gridToTest = (gridToTest[0] + 1,gridToTest[1] - 2)

		# Make sure the piece is not out of bounds
		if(gridToTest[0] > 7 or gridToTest[0] < 0 or gridToTest[1] > 7 or gridToTest[1] < 0):
			# Do nothing
			pass
		else:
			# See if the piece is blocked by any other piece on the same team

			if(gridToTest in self.listOfTeamSquares):
				pass
			else:
				movesCanMake.append(gridToTest)

		# Test -2-1

		# Advance the tested square
		gridToTest = self.getCoordinates()
		gridToTest = (gridToTest[0] - 2,gridToTest[1] - 1)

		# Make sure the piece is not out of bounds
		if(gridToTest[0] > 7 or gridToTest[0] < 0 or gridToTest[1] > 7 or gridToTest[1] < 0):
			# Do nothing
			pass
		else:
			# See if the piece is blocked by any other piece on the same team

			if(gridToTest in self.listOfTeamSquares):
				pass
			else:
				movesCanMake.append(gridToTest)

		# Test -1-2

		# Advance the tested square
		gridToTest = self.getCoordinates()
		gridToTest = (gridToTest[0] - 1,gridToTest[1] - 2)

		# Make sure the piece is not out of bounds
		if(gridToTest[0] > 7 or gridToTest[0] < 0 or gridToTest[1] > 7 or gridToTest[1] < 0):
			# Do nothing
			pass
		else:
			# See if the piece is blocked by any other piece on the same team

			if(gridToTest in self.listOfTeamSquares):
				pass
			else:
				movesCanMake.append(gridToTest)
				
		return(movesCanMake)

class Pawn(Piece):
	"""Creates a pawn piece"""

	def __init__(self, color, x, y):
		"""Creates a pawn version of a piece."""
		super(Pawn,self).__init__(color, x, y)
		self.imageName = self.color + "Pawn.gif"
		self.type = "Pawn"
		# Create piece specific instance variables
		self.queen = False
		self.originalPoint = self.getCoordinates()

		# Determine the direction the pawn must move and the y coordinate it must reach if it is to be a queen
		if(self.getCoordinates()[1] == 1):
			self.direction = 1
			self.queenY = 7
		elif(self.getCoordinates()[1] == 6):
			self.direction = -1
			self.queenY = 0

	def movesCanMakeStart(self, movesCanMake):
		"""Checks for and adds the double turn the pawn can make from its original position."""
		# See if the piece is in its original place
		if(self.getCoordinates() == self.originalPoint):
			# See if the first two spaces are blocked
			# The piece won't go out of bounds because it is in its original square
			if(not((self.getCoordinates()[0],self.getCoordinates()[1] + self.direction) in self.listOfTeamSquares) and not((self.getCoordinates()[0],self.getCoordinates()[1] + self.direction) in self.listOfEnemySquares)):
				if(not((self.getCoordinates()[0],self.getCoordinates()[1] + 2 * self.direction) in self.listOfTeamSquares) and not((self.getCoordinates()[0],self.getCoordinates()[1] + 2 * self.direction) in self.listOfEnemySquares)):
					movesCanMake.append((self.getCoordinates()[0],self.getCoordinates()[1] + 2 * self.direction))
			
	def movesCanMakeRegular(self, movesCanMake):
		"""Gives the moves a pawn can make if it is not a queen."""
		# Check to see if the square in front is occupied, and adds the square otherwise
		if(not((self.getCoordinates()[0],self.getCoordinates()[1] + self.direction) in self.listOfTeamSquares) and not((self.getCoordinates()[0],self.getCoordinates()[1] + self.direction) in self.listOfEnemySquares)):
			# Check if the piece is still in bounds
			if(0 <= self.getCoordinates()[1] + self.direction <= 7):
				movesCanMake.append((self.getCoordinates()[0],self.getCoordinates()[1] + self.direction))

		# Check the diagonals for enemy pieces
		if(not((self.getCoordinates()[0] + 1,self.getCoordinates()[1] + self.direction) in self.listOfTeamSquares) and ((self.getCoordinates()[0] + 1,self.getCoordinates()[1] + self.direction) in self.listOfEnemySquares)):
			# Check the boundary in both axes
			if((0 <= self.getCoordinates()[1] + self.direction <= 7) and (0 <= self.getCoordinates()[0] + 1 <= 7)):
				movesCanMake.append((self.getCoordinates()[0] + 1,self.getCoordinates()[1] + self.direction))

		# Check in both directions

		if(not((self.getCoordinates()[0] - 1,self.getCoordinates()[1] + self.direction) in self.listOfTeamSquares) and ((self.getCoordinates()[0] - 1,self.getCoordinates()[1] + self.direction) in self.listOfEnemySquares)):
			# Check the boundary in both axes
			if((0 <= self.getCoordinates()[1] + self.direction <= 7) and (0 <= self.getCoordinates()[0] - 1 <= 7)):
				movesCanMake.append((self.getCoordinates()[0] - 1,self.getCoordinates()[1] + self.direction))

		# Add the double move the piece can make at the start
		self.movesCanMakeStart(movesCanMake)

	def movesCanMake(self, teamPieces, enemyPieces):
		"""Returns the moves a pawn can make."""
		# Update the piece
		self.update(teamPieces, enemyPieces)
		# Find the moves
		movesCanMake = []
		self.movesCanMakeRegular(movesCanMake)

		return(movesCanMake)
