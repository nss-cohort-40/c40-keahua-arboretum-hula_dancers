# from traits.aquatic import Aquatic
from .environment import Environment
# from animals.river_dolphin import RiverDolphin
# 1. Create function that limits plants CAPACITY (6 plants)
# 2. Create function that limits animals CAPACITY (12 animals)


class River(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.biome_type = "River"
        self.max_capacity_of_animals = 12
        self.max_capacity_of_plants = 6

    def add_animal(self, animal):
        try:
            if animal.aquatic and (animal.exists_in_freshwater):
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-aquatic, or saltwater animals to a river")

    def add_plant(self, plant):
        try:
            if plant.river_plant:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add plants that require brackish water or stagnant water to a river biome")
