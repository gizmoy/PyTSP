from abc import ABC, abstractmethod

class Mutator(ABC):
    """docstring"""
    
    mutationFactor = 0.1

    def __init__(self):
        pass

    @abstractmethod
    def applyMutation(self, problemMap, population):
        pass

    @abstractmethod
    def make(self, problemMap, unit):
        pass
