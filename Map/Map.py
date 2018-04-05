from random import uniform
import json

from Map import City

class Map(object):
	"""Docstring for Map"""

	def __init__(self):
		self.size = 0
		self.cities = []

	def addCity(self, newCity):
		if not isinstance(newCity, City):
			raise Exception("argument is not a City!")
		if not newCity in self.cities:
			newCity.setIndex(self.size)
			self.size += 1
			self.cities.append(newCity)

	@staticmethod
	def generateCNN(size, connections):
		"""
		Generate and connect nearest neighbours.
		Generates map with <size> cities on it, each connected to <connections> nearest neighbours.
		Notice that it doesn't ensure that each node (city) will have exactly <connections> connections, but rather at least that much.
		:param connections: minimum number of neighbours connected to a city
		:return: generated maps
		:type connections: int
		:rtype: Map
		"""

		# Create empty map
		newMap = Map()

		# Generate cities
		for i in range(size):
			newCity = City(uniform(0.0, 1.0), uniform(0.0, 1.0))
			newMap.addCity(newCity)
		newMap.size = size

		# Generate connections
		for city in newMap.cities:
			# Copy cities list and sort by distance from currently evaluated city
			cities = list(newMap.cities)
			cities.sort(key = city.getDistanceTo)
			# Add connections, ommiting self-connection
			for j in range(1, connections + 1):
				city.connect(newMap.cities[cities[j].index])

		# Return created map
		return newMap

	@staticmethod
	def readFromFile(filename):
		"""
		Read map from a file (JSON format)
		"""
		data = None
		try:
			with open(filename, 'r') as data_raw:
				data = json.load(data_raw)
		except IOError as error:
			print("[ERROR] Cannot open file {0} (IOError)".format(filename))
			raise error
			return None
		# except json.JSONDecodeError as error:
		except ValueError as error:
			print("[ERROR] Cannot parse file {0} (JSONDecodeError)".format(filename))
			raise ValueError("Cannot parse file")
			return None
		if not data["cities"] or not data["size"]:
			print("[ERROR] Invalid structure (1).")
			raise ValueError("Invalid structure")
			return None
		newMap = Map()
		newMapSize = int(data["size"])
		try:
			for i in range(newMapSize):
				cityData = data["cities"]["%d" % i]
				newCity = City(float(cityData["positionX"]), float(cityData["positionY"]))
				newCity.setIndex(i)
				for c in cityData["connections"]:
					neighbour = int(c)
					if neighbour < newMapSize:
						newCity.connections.append(int(c))
				newMap.addCity(newCity)
		except KeyError as error:
			print("[ERROR] Invalid structure (2).")
			raise ValueError("Invalid structure")
			return None
		return newMap

	#TODO map verification function, reading/saving from/to file, getDistance etc etc
