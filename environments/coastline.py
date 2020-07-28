from .environment import Environment
#
#
# 1. Create function that limits plants CAPACITY (3 plants)
# 2. Create function that limits animals CAPACITY (15 animals)


class Coastline(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.biome_type = "Coastline"
        self.max_capacity_of_animals = 15
        self.max_capacity_of_plants = 3

    def add_animal(self, animal):
        try:
            if animal.aquatic and (animal.exists_in_saltwater):
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-aquatic, or freshwater animals to a coastline")

    def add_plant(self, plant):
        try:
            if plant.coastline_plant:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add plants that require brackish water or stagnant water to a river biome")
