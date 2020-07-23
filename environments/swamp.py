# from environments import Stagnant
# from environments.environment import Environment
# import sys
# sys.path.append('../')
from animals import Aquatic
from animals import Identifiable
from environments import ContainsAnimals
from environments import ContainsPlants

# from animals.


class Swamp(ContainsAnimals, ContainsPlants, Identifiable):
    # ADD NAME ARG POTENTIALLY
    def __init__(self
                 ):
        # self.name = name
        # WE DON'T NEED THIS RN
        self.inhabitants = []
        ContainsAnimals.__init__(self)
        ContainsPlants.__init__(self)
        Identifiable.__init__(self)

    def animal_count(self):
        return "This place has a bunch of animals in it"

    def addInhabitant(self, item):
        if not isinstance(item, IStagnant):
            raise TypeError(f"{item} is not of type IStagnant")
        self.inhabitants.append(item)

    # def __str__(self):
    #     return self.name
