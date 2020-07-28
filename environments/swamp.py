from .environment import Environment


class Swamp(Environment):
    def __init__(self, name):
        super().__init__(name)
        self.biome_type = "Swamp"
        self.max_capacity_of_animals = 8
        self.max_capacity_of_plants = 12

    def add_animal(self, animal):
        try:
            if animal.exists_in_swamp:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Animal cannot live in the swamp biome.")

    def add_plant(self, plant):
        try:
            if plant.swamp_plant:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                f"A {plant.species} will not survive on the coast!")

    def addInhabitant(self, item):
        if not isinstance(item, IStagnant):
            raise TypeError(f"{item} is not of type IStagnant")
        self.inhabitants.append(item)
