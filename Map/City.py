from math import sqrt

class City(object):
	"""docstring for City"""

	def __init__(self, positionX, positionY):
		if (positionX < 0.0) or (positionX > 1.0) or (positionY < 0.0) or (positionY > 1.0):
			raise Exception("argument out of range!")
		self.index = -1
		self.positionX = positionX
		self.positionY = positionY
		self.connections = []

	def __str__(self):
		return ("{0} ({1}, {2})".format(self.index, self.positionX, self.positionY))

	def setIndex(self, index):
		if index < 0:
			raise Exception("argument out of range!")
		self.index = index

	def setPosition(self, positionX, positionY):
		if (positionX < 0.0) or (positionX > 1.0) or (positionY < 0.0) or (positionY > 1.0):
			raise Exception("argument out of range!")
		self.positionX = positionX
		self.positionY = positionY

	def connect(self, neighbour):
		if not isinstance(neighbour, City):
			raise Exception("argument is not a City!")
		neighbourIndex = neighbour.index
		if neighbourIndex < 0:
			raise Exception("target index out of range!")
		if not (neighbourIndex in self.connections) and (neighbourIndex is not self.index):
			self.connections.append(neighbourIndex)
			neighbour.connect(self)

	def disconnect(self, neighbour):
		if not isinstance(neighbour, City):
			raise Exception("argument is not a City!")
		neighbourIndex = neighbour.index
		if neighbourIndex < 0:
			raise Exception("target index out of range!")
		if (neighbourIndex in self.connections) and (neighbourIndex is not self.index):
			self.connections.remove(neighbourIndex)
			neighbour.disconnect(self)

	def isConnectedTo(self, neighbour):
		neighbourIndex = -1
		if isinstance(neighbour, int):
			neighbourIndex = neighbour
		elif isinstance(neighbour, City):
			neighbourIndex = neighbour.index
		else:
			raise Exception("argument is not a City nor an integer!")
		return (neighbourIndex in self.connections)

	def getDistanceTo(self, city):
		if not isinstance(city, City):
			raise Exception("argument is not a City!")
		distX = self.positionX - city.positionX
		distY = self.positionY - city.positionY
		return sqrt(distX**2 + distY**2)
