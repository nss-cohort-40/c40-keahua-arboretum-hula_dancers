from animals.animal import Animal
from identifiable import Identifiable


class Nene_goose(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        Identifiable.__init__(self)
        self.__prey = ["Berries", "Clovers", "Orchard Grass"]
        self.minimum_age_in_months = 7
        self.exists_in_grassland = True
        self.biome_type = ["Grassland"]

    @property
    def prey(self):
        return self.__prey
