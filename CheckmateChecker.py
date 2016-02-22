# CheckmateChecker.py
# Written by: Shasta Ramachandran
# Date: 2/22/2016
# Checks checkmate given a situation

class CheckMateChecker:

	def __init__(self):
		"""Creates an instance of a checkmate checker. The checker is reusable over many configurations."""
		pass

	def update(self, team1, team2):
		"""Stores two teams as instance variables for use. The first listed team is the team that will be tested, the second is the enemy team."""
		# Store teams and kings
		self.team1 = team1
		self.king1 = team1[0]
		self.team2 = team2
		self.king2 = team2[0]

		# Store the list of all coordinates, as a reserve
		self.coords1 = []
		for piece in team1:
			self.coords1.append(piece.getCoordinates)
		self.coords2 = []
		for piece in team2:
			self.coords2.append(piece.getCoordinates)

		# Store the list of all moves that can be made
		self.moves1 = []
		for piece in team1:
			self.moves1 += piece.movesCanMake()
		self.moves2 = []
		for piece in team2:
			self.moves2 += piece.movesCanMake()

	def checkCheckInternal(self):
		"""Checks the stored instance variables for check."""
		# Check 
		if(self.king1 in self)

	def testForCheckmate(self,team,enemy):
		"""Tests the first inputed team for checkmate."""
		# Store the list of all coordinates
		self.coords1 = []
		for piece in team:
			self.coords1.append(piece.getCoordinates)
		# Find the set of all moves for team
		self.movesTeamCanMake = []


		for move in piece.movesCanMake(whitePieces,blackPieces):
                        gui.highlightSelectedSquare(move)
                    square = gui.getInput()
                    if square in piece.movesCanMake(whitePieces,blackPieces):
                        piece.setCoordinates(square)
                        piece.draw(gui)
