import random

from Operators.Mutation import Mutator
from Map import City
from Population import Population, Unit

class DisplacementMutator(Mutator):
    """docstring"""

    def __init__(self, mutationProbability):
        super().__init__()
        self.mutationProbability = float(mutationProbability)

    def applyMutation(self, problemMap, population):
        newUnits = []
        for unit in population.units:
            if random.random() < self.mutationProbability:
                newUnits.append(self.mutate(problemMap, unit))
            else:
                newUnits.append(unit)
        return Population(population.size, newUnits)

    def make(self, problemMap, unit):
        """
        :param problemMap:
        :return unit:
        """
        if random.random() < self.mutationProbability:
            return self.mutate(problemMap, unit)
        else:
            return unit

    def mutate(self, problemMap, unit):
        """
        :param problemMap:
        :return unit:
        """
        pathLength = len(unit.path)
        found = False

        while not found:
            # get a random place where to begin the subpath to displace
            begin = random.randrange(pathLength)
            # get a random length (max half the length of path - anything more would be equal to displacing the rest of path)
            length = random.randrange(pathLength/2)
            # get a random shift we're to displace the subpath by
            shift = random.randrange(pathLength) - 1
            shiftTries = 0

            while not found and shiftTries < pathLength:
                shift += 1
                shiftTries += 1

                end = (begin + length - 1) % pathLength

                beginCity = problemMap.cities[unit.path[begin]]
                beginCityPrev = problemMap.cities[unit.path[begin - 1]]
                endCity = problemMap.cities[unit.path[end]]
                endCityNext = problemMap.cities[unit.path[(end + 1) % pathLength]]
                endCityNewNext = problemMap.cities[unit.path[(end + shift) % pathLength]]

                if not beginCityPrev.isConnectedTo(endCityNext):
                    continue
                if not beginCity.isConnectedTo(endCityNext):
                    continue
                if not endCity.isConnectedTo(endCityNewNext):
                    continue
                found = True

            if found:
                end = (begin + length - 1) % pathLength
                if end < begin:
                    tmp = end
                    end = begin
                    begin = tmp
                path = unit.path[: begin] + unit.path[end + 1 : end + 1 + shift] + unit.path[begin : end + 1] + unit.path[end + 1 + shift :]
                return Unit(problemMap, path)
