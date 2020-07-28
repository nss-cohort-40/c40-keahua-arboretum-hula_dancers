# from traits.aquatic import Aquatic
from .environment import Environment
# from animals.river_dolphin import RiverDolphin
# 1. Create function that limits plants CAPACITY (6 plants)
# 2. Create function that limits animals CAPACITY (12 animals)


class River(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.biome_type = "River"
        self.max_capacity_animals = 12

    def add_animal(self, animal):
        try:
            if (animal.aquatic and animal.exists_in_freshwater) or animal.exists_in_river:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Animal cannot add non-aquatic, or saltwater animals to a river")

    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add plants that require brackish water or stagnant water to a river biome")
