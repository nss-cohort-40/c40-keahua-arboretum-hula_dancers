from .environment import Environment


class Forest(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.biome_type = "Forest"
        self.max_capacity_of_animals = 20
        self.max_capacity_of_plants = 32

    def add_animal(self, animal):
        try:
            if animal.exists_in_forest:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Animal cannot exist in the swamp biome.")

    def add_plant(self, plant):
        try:
            if plant.forest_plant:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                f"A {plant.species} will not survive in a forest biome. Please choose a different biome.")
