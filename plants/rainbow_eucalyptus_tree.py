from plants import Plant
from identifiable import Identifiable
from .forest_plant import ForestPlant


class RainbowEucalyptusTree(Plant, Identifiable, ForestPlant):

    def __init__(self):
        Plant.__init__(self)
        Identifiable.__init__(self)
        ForestPlant.__init__(self)
        self.sunlight = "shade"
        self.species = "Rainbow Eucalyptus Tree"
