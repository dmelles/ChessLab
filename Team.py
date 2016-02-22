# Team.py
# Written by: ShastaRamachandran
# Date: 2/21/2016
# Provies a team functionality to a list of pieces

class Team:

	def __init__(self):
		"""Creates a team."""
		self.pieces = []

	def addPieces(self, pieces):
		"""Adds pieces or a piece to the team."""
		# Determine whether to add 1 or many pieces
		if(type(pieces) == list):
			self.pieces += pieces

		else:
			self.pieces.append(pieces)

	def movesCanMake(self,)