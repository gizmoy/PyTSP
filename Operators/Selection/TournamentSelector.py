import random

from Operators.Selection import Selector
from Population import Population

class TournamentSelector(Selector):
    """docstring"""

    def __init__(self, tournamentSize = 4, elitismFactor = 0):
        super().__init__()
        self.tournamentSize = tournamentSize
        self.elitismFactor = elitismFactor

    def applySelection(self, population, newPopulationSize):
        return Population(newPopulationSize, self.make(population, newPopulationSize))

    def make(self, population, newPopulationSize):
        """
        Process population.
        Winner of a single tournament is excluded from next ones.
        :param population:
        :param newPopulationSize:
        :return: list of selected Units
        """
        units = population.units[:]
        newUnits = []

        for i in range(self.elitismFactor):
            elite = population.bestUnit(i)
            newUnits.append(elite)
            #TODO: verify if this works
            units.remove(elite)
        while len(newUnits) < newPopulationSize and len(units):
            tournamentPopulation = Population()
            while tournamentPopulation.size < self.tournamentSize and len(units):
                unit = random.choice(units)
                tournamentPopulation.addUnitAndExpand(unit)
            selectedUnit = tournamentPopulation.bestUnit()
            units.remove(selectedUnit)
            newUnits.append(selectedUnit)
        return newUnits
