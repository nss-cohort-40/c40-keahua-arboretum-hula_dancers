from plants.plant import Plant
from identifiable import Identifiable


class BlueJadeVine(Plant, Identifiable):
    def __init__(self):
        Plant.__init__(self)
        Identifiable.__init__(self)
        self.sunlight = "partial"
        self.species = "Blue Jade Vine"
