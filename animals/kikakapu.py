from animals.animal import Animal
from identifiable import Identifiable

class kikakapu(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Kickakapu")
        Identifiable.__init__(self)
        Animal.prey = {}