from animals.animal import Animal
from identifiable import Identifiable


class Hawaiian_happyface_spider(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Hawaiian Happy-face Spider")
        Identifiable.__init__(self)
        Animal.prey = {}
        self.minimum_age_in_months = .5
