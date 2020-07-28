from .environment import Environment


class River(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.biome_type = "River"
        self.max_capacity_of_animals = 12
        self.max_capacity_of_plants = 6

    def add_animal(self, animal):
        try:
            if animal.exists_in_river:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Animal cannot add non-aquatic, or saltwater animals to a river")

    def add_plant(self, plant):
        try:
            if plant.river_plant:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add plants that require brackish water or stagnant water to a river biome")
