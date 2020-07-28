from animals.animal import Animal
from identifiable import Identifiable


class Opeapea(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Ope\'ape\'a")
        Identifiable.__init__(self)
        self.__prey = ["Mosquitoes", "Beetles", "Moths"]
        self.minimum_age_in_months = 5
