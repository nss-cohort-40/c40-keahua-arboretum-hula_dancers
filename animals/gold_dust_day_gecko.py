from animals.animal import Animal
from identifiable import Identifiable
from traits.terrestrial import Terrestrial
from traits.walking import Walking


class Gold_dust_day_gecko(Animal, Identifiable, Terrestrial, Walking):

    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko")
        Identifiable.__init__(self)
        self.__prey = ["Crickets", "Beetles", "Flies"]
        self.minimum_age_in_months = 2
        Terrestrial.__init__(self)
        Walking.__init__(self, leg_count=4)
        self.exists_in_forest = True

    @property
    def prey(self):
        return self.__prey
