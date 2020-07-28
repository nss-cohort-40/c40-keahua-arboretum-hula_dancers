from plants import Plant
from identifiable import Identifiable
from .mountain_plant import MountainPlant


class MountainAppleTree(Plant, Identifiable, MountainPlant):

    def __init__(self):
        Plant.__init__(self)
        Identifiable.__init__(self)
        MountainPlant.__init__(self)
        self.sunlight = "partial"
        self.species = "Mountain Apple Tree"
