# CheckmateChecker.py
# Written by: Shasta Ramachandran
# Date: 2/22/2016
# Checks checkmate given a situation

class CheckMateChecker:

	def __init__(self):
		"""Creates an instance of a checkmate checker. The checker is reusable over many configurations."""
		pass

	def update(self, team1, team2):
		"""Stores two teams as instance variables for use."""
		# Store teams and kings
		self.team1 = team1
		self.king1 = team1[0]
		self.team2 = team2
		self.king2 = team2[0]

	def testForCheckmate(self,team,enemy):
		"""Tests the first inputed team for checkmate."""
		# Store the list of all coordinates
		for i in range 
		# Find the set of all moves for team
		self.movesTeamCanMake = []


		for move in piece.movesCanMake(whitePieces,blackPieces):
                        gui.highlightSelectedSquare(move)
                    square = gui.getInput()
                    if square in piece.movesCanMake(whitePieces,blackPieces):
                        piece.setCoordinates(square)
                        piece.draw(gui)
