from PyQt5.QtCore import QThread, pyqtSignal

from Population import Population, Unit

class PopulationGenerator(QThread):
    populationGenerated = pyqtSignal(Population)
    populationGenerationFailed = pyqtSignal(Exception)

    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.problemMap = None
        self.populationSize = 0
        self.method = None

    def setGenerationParameters(self, problemMap, populationSize = 0, method = None):
        self.problemMap = problemMap
        self.populationSize = populationSize
        self.method = method

    def run(self):
        if not self.problemMap:
            self.populationGenerationFailed.emit(Exception("No problem map"))
            return
        if not self.populationSize or not self.method:
            self.populationGenerationFailed.emit(Exception("Missing parameters"))
            return

        units = []
        try:
            while len(units) < self.populationSize:
                unit = None
                if self.method == "rand":
                    unit = Unit.generateUnitRand(self.problemMap)
                elif self.method == "ds":
                    unit = Unit.generateUnitDSRandom(self.problemMap)
                else:
                    raise Exception("Unknown method")

                if unit not in units:
                    units.append(unit)
        except Exception as e:
            self.populationGenerationFailed.emit(e)
            return

        population = Population(self.populationSize, units)
        self.populationGenerated.emit(population)
