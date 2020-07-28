# from environments import Stagnant
# sys.path.append('../')
from .environment import Environment
from environments import ContainsPlants
# from animals import Aquatic
# 1. Create function that limits plants CAPACITY (12 plants)
# 2. Create function that limits animals CAPACITY (8 animals)


class Swamp(Environment):
    def __init__(self, name):
        super().__init__(name)
        self.biome_type = "Swamp"

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.exists_in_freshwater:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-aquatic, or saltwater animals to a swamp")

    def add_plant(self, plant):
        try:
            if plant.swamp_plant:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                f'A {plant.species} will not be able to live a fraction of its best life in a swamp.')

    # def addInhabitant(self, item):
    #     if not isinstance(item, IStagnant):
    #         raise TypeError(f"{item} is not of type IStagnant")
    #     self.inhabitants.append(item)

    # def __str__(self):
    #     return self.name
