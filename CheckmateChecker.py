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
			self.coords1.append(piece.getCoordinates())
		self.coords2 = []
		for piece in team2:
			self.coords2.append(piece.getCoordinates())

		# Store the list of all moves that can be made
		self.moves1 = []
		for piece in team1:
			self.moves1 += piece.movesCanMake()
		self.moves2 = []
		for piece in team2:
			self.moves2 += piece.movesCanMake()

	def pseudoUpdate(self,team1,team2):
		"""Updates the teams, but keeps the reserve coordinates the same."""
		# Store the coordinates
		coords1 = self.coords1
		coords2 = self.coords2

		# Update
		self.update(team1,team2)

		# Re-install the coordinates
		self.coords1 = coords1
		self.coords2 = coords2


	def checkCheckInternal(self):
		"""Checks the stored instance variables for check."""
		# Check to see if the king is in the moves the enemy can make.
		return(self.king1.getCoordinates() in self.moves2)

	def Checkmate(self, team, enemy):
		"""Tests the first inputed team for checkmate."""
		# Update
		self.update(team, enemy)
		checkmate = True
		# Cycle through all the teams moves and test for check
		while True: # Loop to allow for a break
			for piece in team1:
				for move in piece.movesCanMake():
					# Move the piece
					piece.setCoordinates(move)
					# Update the teams, but not the reserve coordinates
					team1 = self.team1
					team2 = self.team2
					self.pseudoUpdate(team1,team2)
					# Check for check
					if(self.checkCheckInternal()):
						# No change
						pass
					else:
						# Set to false and break
						checkmate = False
						break

		# Reset the coordinates
		for i in range(len(team1)):
			team1[i].setCoordinates(coords1[i])
		for i in range(len(team2)):
			team2[i].setCoordinates(coords1[i])

		# Return a true or false
		return(checkmate)

	def Check(self, team, enemy):
		"""Tests the first inputed team for check."""
		# Update the team
		self.update(team, enemy)
		return(self.checkCheckInternal())