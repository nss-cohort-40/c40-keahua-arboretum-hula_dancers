from animals.animal import Animal
from identifiable import Identifiable


class Ulae(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Ulae")
        Identifiable.__init__(self)
        Animal.prey = {}
        self.minimum_age_in_months = 1
        self.exists_in_coastline = True
