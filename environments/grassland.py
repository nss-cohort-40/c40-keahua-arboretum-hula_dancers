from .environment import Environment
#
#
# 1. Create function that limits plants CAPACITY (16 plants)
# 2. Create function that limits animals CAPACITY (22 animals)


class Grassland(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.biome_type = "Grassland"

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypertonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-aquatic, or saltwater animals to a river")

    def add_plant(self, plant):
        try:
            if len(self.plants) >= 16:
                print(f'\n****      That biome is not large enough      ****')
                input(f'****        Please choose another one       ****')
            if plant.grassland_plant and len(self.plants) < 16:
                self.plants.append(plant)
                print(
                    f'\nNOICE. You added a {plant.species} to the {self.name} {self.biome_type}!')
                input("\n** Press Enter **")
        except AttributeError:
            raise AttributeError(
                f'A {plant.species} does not grow in grassland biomes.')
