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
        self.__prey = ["Trout", "Mackarel", "Salmon", "Sardine"]
        self.minimum_age_in_months = 13
        self.cell_type = "both"

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The dolphin ate {prey} for a meal')
        else:
            print(f'The dolphin rejects the {prey} ')

    def __str__(self):
        return f'Dolphin {self.id}. Eeee EeeEEeeeeEE!'
