from Population.Population import Population

class Evolution(object):
    """docstring for Evolution"""

    def __init__(self, problemMap, population, selector, crosser, mutator):
        self.problemMap = problemMap
        self.population = population
        self.selector = selector
        self.crosser = crosser
        self.mutator = mutator

    def evolve(self):
        childrenPopulation = self.crosser.applyCrossing(self.problemMap, self.population, self.population.size, self.mutator)
        # childrenPopulation = self.mutator.applyMutation(self.problemMap, childrenPopulation)
        sumPopulation = Population(2 * self.population.size, self.population.units + childrenPopulation.units)
        return self.selector.applySelection(sumPopulation, self.population.size)

    def make(self, iterations):
        """
        :param iterations:
        :return:
        """
        for i in range(iterations):
            # evolve one generation
            newPopulation = self.evolve()

            # change options
            #self.mutator.changeParams()
            #self.selector.changeParams()

            # print results
            print("\nGeneration {0}: ".format(i+1))
            for i in range(len(newPopulation.units)):
                unit = newPopulation.units[i]
                print("{0}: {1}".format(i, unit.fitness))

            self.population = newPopulation
            input('Press enter for next generation...')

        return self.population
