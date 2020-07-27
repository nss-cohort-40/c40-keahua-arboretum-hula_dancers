# from environments import Stagnant
# sys.path.append('../')
from .environment import Environment
from environments import ContainsPlants
# from animals import Aquatic
# 1. Create function that limits plants CAPACITY (12 plants)
# 2. Create function that limits animals CAPACITY (8 animals)


class Swamp(Environment, ContainsPlants):
    def __init__(self, name):
        Environment.__init__(self, name)
        ContainsPlants.__init__(self)
        self.biome_type = "Swamp"

    # def addInhabitant(self, item):
    #     if not isinstance(item, IStagnant):
    #         raise TypeError(f"{item} is not of type IStagnant")
    #     self.inhabitants.append(item)

    # def __str__(self):
    #     return self.name
