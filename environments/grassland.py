from .environment import Environment


class Grassland(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.biome_type = "Grassland"
        self.max_capacity_of_animals = 22
        self.max_capacity_of_plants = 16

    def add_animal(self, animal):
        try:
            if animal.exists_in_grassland:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Animal cannot live in the grassland biome")

    def add_plant(self, plant):
        try:
            if plant.grassland_plant:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                f'A {plant.species} does not grow in grassland biomes.')
