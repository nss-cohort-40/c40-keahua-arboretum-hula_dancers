from animals.animal import Animal
from identifiable import Identifiable


class Kikakapu(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Kīckākapu")
        Identifiable.__init__(self)
        Animal.prey = {}
        self.minimum_age_in_months = 1
        self.IStagnant = True
