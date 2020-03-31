class Arena:
	def __init__(self, player, pieces):
		self.player = player
		self.pieces = pieces

		self.level = 0
		self.score = 0
		self.lines = 0

		self.grid = Grid()
		self.stats = Stats(pieces)

		self.piece = Piece()

	# Receives a JSON object with the new contents of the arena.
	def update(self, data):
		self.level = data['level']
		self.score = data['score']
		self.lines = data['lines']

		self.grid.update(data['grid'])
		self.stats.update(data['stats'], self.pieces)

	# Receives the new position of the falling piece of this arena.
	def updatePieceFromClient(self, data):
		self.piece.updateFromServer(data)

class Grid:
	def __init__(self):
		self.squares = []
		for i in range(20):
			self.squares.append([])
			for j in range(10):
				self.squares[i].append(False)

	# Receives a JSON object with the new contents of the grid.
	def update(self, data):
		for i in range(20):
			for j in range(10):
				self.squares[i][j] = data[i][j]

class Stats:
	def __init__(self, pieces):
		self.numbers = {}
		for piece in pieces:
			self.numbers[piece] = 0

	# Receives a JSON object with the new stats.
	def update(self, data, pieces):
		for piece in pieces:
			self.numbers[piece] = data[piece]

class Piece:
	def __init__(self):
		self.squares = []

	# Receives the update JSON from the server.
	def updateFromServer(self, data):
		self.squares = []
		for square in data['squares']:
			self.squares.append(square)