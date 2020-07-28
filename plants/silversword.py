from plants import Plant
from identifiable import Identifiable
from .grassland_plant import GrasslandPlant


class Silversword(Plant, Identifiable, GrasslandPlant):

    def __init__(self):
        Plant.__init__(self)
        Identifiable.__init__(self)
        GrasslandPlant.__init__(self)
        self.sunlight = "full"
        self.species = "Silversword"
