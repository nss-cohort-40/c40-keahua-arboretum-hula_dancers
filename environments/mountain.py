from .environment import Environment
#
#
# 1. Create function that limits plants CAPACITY (4 plants)
# 2. Create function that limits animals CAPACITY (6 animals)


class Mountain(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.biome_type = "Mountain"

    def add_animal(self, animal):
        try:
            if animal.exists_in_mountain:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Animal cannot exist in mountain biome")

    def add_plant(self, plant):
        try:
            if plant.mountain_plant:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                f"A {plant.species} will not survive in the high altitude of the mountains.")
