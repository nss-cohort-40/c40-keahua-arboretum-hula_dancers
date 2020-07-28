from .environment import Environment
from environments import ContainsPlants
#
# 1. Create function that limits plants CAPACITY (32 plants)
# 2. Create function that limits animals CAPACITY (20 animals)
#


class Forest(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.biome_type = "Forest"

    def add_animal(self, animal):
        try:
            if animal.terrestrial or animal.walking or animal.flying:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-aquatic, or saltwater animals to a river")

    def add_plant(self, plant):
        try:
            if plant.species == "Rainbow Eucalyptus Tree":
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add plants that require brackish water or stagnant water to a river biome")
