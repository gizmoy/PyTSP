from random import choice

class Unit(object):
    """docstring for Population/Unit"""

    cost = 0

    def __init__(self, problemMap, path, cost = 0):
        #TODO: add parameter checks

        self.map = problemMap
        self.path = path
        self.cost = cost
        self.length = 0.0
        self.fitness = 0.0

        nextCity = self.map.cities[self.path[0]]
        for i in range(-1, len(self.path)-1):
            currentCity = nextCity
            nextCity = self.map.cities[self.path[i+1]]
            self.length += currentCity.getDistanceTo(nextCity)

        self.fitness = 1.0 / self.length

    @staticmethod
    def generateUnitRand(problemMap):
        """
        Generate an unit by starting from city0 and randomly selecting unused neighbour to connect to.
        If there is no such one, begin anew (random is quite inefficient).

        """
        Unit.cost = 0
        while True:
            Unit.cost += 1
            currentIndex = 0
            path = [0]
            while len(path) < problemMap.size:
                currentCity = problemMap.cities[currentIndex]
                neighbours = [i for i in currentCity.connections if not i in path]
                if len(neighbours) == 0:
                    break
                currentIndex = choice(neighbours)
                path.append(currentIndex)
            if len(path) < problemMap.size:
                continue
            firstCity = problemMap.cities[path[0]]
            lastCity = problemMap.cities[path[problemMap.size - 1]]
            if not firstCity.isConnectedTo(lastCity):
                continue
            unit = Unit(problemMap, path, Unit.cost)
            if(unit.verify()):
                return unit
            else:
                print("Generated invalid unit!!!")

    @staticmethod
    def generateUnitDSRandom(problemMap):
        """
        Generate an unit by doing random choice depth search.
        Sloooooow.
        """

        Unit.cost = 0
        def _generatePath(problemMap, path, targetLength):
            Unit.cost += 1
            firstCity = problemMap.cities[path[0]]
            currentCity = problemMap.cities[path[-1]]

            if len(path) == targetLength:
                if firstCity.isConnectedTo(currentCity):
                    return path
                else:
                    return None

            firstCityNeighbours = [i for i in firstCity.connections if not i in path]
            if len(firstCityNeighbours) == 1:
                return _generatePath(problemMap, [firstCityNeighbours[0]] + path, targetLength)

            usableNeighbours = [i for i in currentCity.connections if not i in path]

            selectedNeighbour = -1
            while len(usableNeighbours) > 0:
                neighbour = choice(usableNeighbours)
                newPath = path[:]
                newPath.append(neighbour)
                newPath = _generatePath(problemMap, newPath, targetLength)
                if newPath is not None:
                    return newPath
                usableNeighbours.remove(neighbour)
            return None

        path = _generatePath(problemMap, [0], problemMap.size)
        return Unit(problemMap, path, Unit.cost)

    @staticmethod
    def generateUnitDSGreedy(problemMap):
        """
        Generate an unit by doing greedy depth search.

        """

        Unit.cost = 0
        def _generatePath(problemMap, path, targetLength):
            Unit.cost += 1
            currentCity = problemMap.cities[path[-1]]
            firstCity = problemMap.cities[path[0]]

            if len(path) == targetLength:
                if firstCity.isConnectedTo(currentCity):
                    return path
                else:
                    return None

            firstCityNeighbours = [i for i in firstCity.connections if not i in path]
            if len(firstCityNeighbours) == 1:
                return _generatePath(problemMap, [firstCityNeighbours[0]] + path, targetLength)

            usableNeighbours = [i for i in currentCity.connections if not i in path]
            usableNeighbours.sort(key = lambda neighbour: currentCity.getDistanceTo(problemMap.cities[neighbour]))

            selectedNeighbour = -1
            while len(usableNeighbours) > 0:
                neighbour = usableNeighbours[0]
                newPath = path[:]
                newPath.append(neighbour)
                newPath = _generatePath(problemMap, newPath, targetLength)
                if newPath is not None:
                    return newPath
                usableNeighbours.remove(neighbour)
            return None

        path = _generatePath(problemMap, [0], problemMap.size)
        return Unit(problemMap, path, Unit.cost)

    @staticmethod
    def verifyUnit(unit, problemMap):
        if len(unit.path) != problemMap.size:
            return False

        visited = [ False for i in range(problemMap.size) ]
        for c in unit.path:
            visited[c] = True

        return (False not in visited)

    def verify(self):
        return Unit.verifyUnit(self, self.map)
