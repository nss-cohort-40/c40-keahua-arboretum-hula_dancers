# from traits.aquatic import Aquatic
from .environment import Environment
# from animals.river_dolphin import RiverDolphin


class River(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.biome_type = "River"

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypertonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-aquatic, or saltwater animals to a river")

    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add plants that require brackish water or stagnant water to a river biome")
