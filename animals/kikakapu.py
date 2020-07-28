from animals.animal import Animal
from identifiable import Identifiable


class Kikakapu(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Kīkākapu")
        Identifiable.__init__(self)
        self.__prey = ["Trout", "Mackerel", "Salmon"]
        self.minimum_age_in_months = 1
        self.IStagnant = True
        self.exists_in_swamp = True
        self.exists_in_river = True

    @property
    def prey(self):
        return self.__prey
