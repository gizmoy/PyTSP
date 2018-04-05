import random
from copy import deepcopy

from Operators.Crossing import Crosser
from Population import Population, Unit

class EdgeCrosser(Crosser):
    """docstring"""

    cost = 0

    def __init__(self, parentsCount, useDepthSearch = False):
        super().__init__()
        self.parentsCount = parentsCount
        self.useDepthSearch = useDepthSearch

    def applyCrossing(self, problemMap, population, newPopulationSize, mutator = None):
        children = []
        while len(children) < newPopulationSize:
            parents = []
            possibleParents = population.units[:]
            while len(parents) < self.parentsCount:
                parent = random.choice(possibleParents)
                possibleParents.remove(parent)
                parents.append(parent)
            childUnit = self.make(problemMap, parents)

            if mutator is not None:
                childUnit = mutator.make(problemMap, childUnit)

            duplicate = False
            for unit in children:
                if duplicate:
                    break
                if childUnit.path == unit.path:
                    duplicate = True
            for unit in population.units:
                if duplicate:
                    break
                if childUnit.path == unit.path:
                    duplicate = True

            if not duplicate:
                children.append(childUnit)
        return Population(newPopulationSize, children)

    def make(self, problemMap, units):
        """
        :param problemMap:
        :param units:
        :return unit:
        TODO: make static?
        """
        paths = [unit.path for unit in units]

        adjList = self.makeAdjacencyList(problemMap, paths)
        path = None
        if self.useDepthSearch:
            path = self.makePathDS(adjList)
            # print("Cost: {0}".format(EdgeCrosser.cost))
        else:
            path = self.makePathRand(adjList)
            # print("Cost: {0}".format(EdgeCrosser.cost))

        ##TODO: verify obtained path

        return Unit(problemMap, path)

    def makePathRand(self, adjList):
        """
        :param adjList: adjacency list
        :return path: new path
        """

        EdgeCrosser.cost = 0
        while True:
            EdgeCrosser.cost += 1
            src = 0
            path = []

            while len(path) != len(adjList):
                path.append(src)

                srcList = adjList[src][:]
                curr = random.choice(srcList)

                while curr in path:
                    srcList.remove(curr)
                    if len(srcList) == 0:
                        break
                    curr = random.choice(srcList)
                if len(srcList) == 0:
                    break

                src = curr
            if len(path) != len(adjList):
                continue

            return path

    def makePathDS(self, adjList):
        """
        :param adjList: adjacency list
        :return path: new path
        """

        EdgeCrosser.cost = 0
        def _makeSubpath(path, adjList):
            EdgeCrosser.cost += 1

            if len(path) == len(adjList):
                if path[-1] in adjList[path[0]]:
                    return path
                else:
                    return None

            firstCityConnections = [c for c in adjList[path[0]] if not c in path]
            if len(firstCityConnections) == 1:
                newStart = adjList[path[0]][0]
                return _makeSubpath([newStart] + path, adjList)

            connections = [c for c in adjList[path[-1]] if not c in path]
            while len(connections) > 0:
                nextCity = random.choice(connections)
                subPath = _makeSubpath(path + [nextCity], adjList)
                if subPath is not None:
                    return subPath
                connections.remove(nextCity)
            return None
        return _makeSubpath([0], adjList)

    def makeAdjacencyList(self, problemMap, paths):
        """
        :param problemMap:
        :param paths: list of paths from Units chosen for crossing
        :return adjList: adjacency list (object mapping city index -> list of adjacencies)
        """

        adjList = {i.index: [] for i in problemMap.cities}
        #should be equivalent to this matrix:
        #adjList = [[] for i in range(problemMap.size)]

        for path in paths:
            for j in range(len(path)):
                index = path[j]
                prevIndex = path[j-1]
                nextIndex = path[(j+1) % len(path)]
                if prevIndex not in adjList[index]:
                    adjList[index].append(prevIndex)
                if nextIndex not in adjList[index]:
                    adjList[index].append(nextIndex)

        for index in range(problemMap.size):
            while index in adjList[index]:
                adjList[index].remove(index)

        return adjList
