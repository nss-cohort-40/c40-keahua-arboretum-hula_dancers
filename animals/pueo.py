from animals.animal import Animal
from identifiable import Identifiable
# from environments.grassland import Grassland
# from environments.forest import Forest


class Pueo(Animal, Identifiable):  # add Freshwater

    def __init__(self):
        Animal.__init__(self, "Pueo")
        # Grassland.__init__(self)
        # Forest.__init__(self)
        Identifiable.__init__(self)
        self.__prey = ["Mice", "Rats"]
        self.minimum_age_in_months = 8

    @property
    def prey(self):
        return self.__prey
