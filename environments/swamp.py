# from environments import Stagnant
# sys.path.append('../')
from .environment import Environment
# from animals import Aquatic


class Swamp(Environment):
    def __init__(self, name):
        super().__init__(name)

    def addInhabitant(self, item):
        if not isinstance(item, IStagnant):
            raise TypeError(f"{item} is not of type IStagnant")
        self.inhabitants.append(item)

    # def __str__(self):
    #     return self.name
