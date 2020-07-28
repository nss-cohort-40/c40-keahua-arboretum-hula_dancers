from .contains_animals import ContainsAnimals
from .contains_plants import ContainsPlants
from identifiable import Identifiable


class Environment(ContainsAnimals, ContainsPlants, Identifiable):

    def __init__(self, name):
        ContainsAnimals.__init__(self)
        ContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.max_capacity_of_animals = 0
        self.max_capacity_of_plants = 0
        self.name = name

    # NOT SURE IF THIS FUNC IS NEEDED?
    # def animal_count(self):
    #     return f`This place has {len(animals)} animals in it`
# SARAH THINKS WE SHOULD CHECK AT CAPACITY HERE

    def plant_max_capacity(self, plant):
        if len(self.plants) >= (self.max_capacity_of_plants):
            print(f'\n****      That biome is not large enough      ****')
            input(f'****        Please choose another one       ****')
        elif len(self.plants) < (self.max_capacity_of_plants):
            self.add_plant(plant)
            input("> ")
