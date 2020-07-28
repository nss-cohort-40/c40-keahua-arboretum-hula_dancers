from animals.animal import Animal
from identifiable import Identifiable
from traits.freshwater import Freshwater
from traits.saltwater import Saltwater


class RiverDolphin(Animal, Freshwater, Identifiable, Saltwater):

    def __init__(self):
        Animal.__init__(self, "River dolphin")
        Saltwater.__init__(self)
        Freshwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = ["Trout", "Mackarel", "Salmon", "Sardines"]
        self.minimum_age_in_months = 13
        self.exists_in_coastline = True
        self.exists_in_river = True

    @property
    def prey(self):
        return self.__prey
