from animals.animal import Animal
from identifiable import Identifiable


class Opeapea(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Ope\'ape\'a")
        Identifiable.__init__(self)
        Animal.prey = {}
        self.minimum_age_in_months = 5
