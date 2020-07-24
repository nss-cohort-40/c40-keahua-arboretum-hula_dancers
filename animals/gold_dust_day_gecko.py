from animals.animal import Animal
from identifiable import Identifiable

class Gold_dust_day_gecko(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko")
        Identifiable.__init__(self)
        Animal.prey = {}
