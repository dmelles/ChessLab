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

	def killPiece(self, piece):
		"""Kills one of the team's pieces."""
		# Find the piece
		order = self.pieces.index(piece)
		# Kill the piece
		self.pieces[order].kill()
		# Remove the piece from the list
		del(self.pieces[order])

	def movesCanMake(self,enemyPieces):
		"""Returns the moves the team can make."""
		movesCanMake = []
		# Loop through pieces
		for piece in self.pieces:
			# Generate teamPieces
			teamPieces = self.pieces
			order = self.pieces.index(piece)
			del(teamPieces[order])

			# Run movesCanMake
			movesCanMake.append(piece.movesCanMake(teamPieces,enemyPieces))

		return movesCanMake