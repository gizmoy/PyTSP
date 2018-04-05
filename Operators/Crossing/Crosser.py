from abc import ABC, abstractmethod

class Crosser(ABC):
    """docstring"""

    def __init__(self):
        pass

    @abstractmethod
    def make(self, problemMap, units):
        pass
