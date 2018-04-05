from abc import ABC, abstractmethod

class Selector(ABC):
    """docstring"""

    def __init__(self):
        pass

    @abstractmethod
    def make(self, population, selectSize, tSize):
        pass
