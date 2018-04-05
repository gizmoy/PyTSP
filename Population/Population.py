from Population import Unit

class Population(object):
    """docstring"""

    def __init__(self, size = 0, units = None):
        self.size = size
        if units is None:
            self.units = []
            self.sorted = False
        else:
            self.units = units
            self.units.sort(key=lambda unit: unit.fitness, reverse=True)
            self.sorted = True

    def addUnit(self, unit):
        if len(self.units) >= self.size:
            return    
        if unit in self.units:
            return
        self.units.append(unit)
        self.sorted = False

    def addUnitAndExpand(self, unit):
        if unit in self.units:
            return
        self.units.append(unit)
        self.size += 1
        self.sorted = False

    def bestUnit(self, position = 0):
        if position >= self.size:
            position = self.size - 1
        if self.sorted == False:
            self.units.sort(key = lambda unit: unit.fitness, reverse=True)
            self.sorted = True

        return self.units[position]
