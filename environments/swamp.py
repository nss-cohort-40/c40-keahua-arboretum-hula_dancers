# from environments import Stagnant
# sys.path.append('../')
from .environment import Environment
# 1. Create function that limits plants CAPACITY (12 plants)
# 2. Create function that limits animals CAPACITY (8 animals)


class Swamp(Environment):
    def __init__(self, name):
        super().__init__(name)
        self.biome_type = "Swamp"

    def addInhabitant(self, item):
        if not isinstance(item, IStagnant):
            raise TypeError(f"{item} is not of type IStagnant")
        self.inhabitants.append(item)

    # def __str__(self):
    #     return self.name
