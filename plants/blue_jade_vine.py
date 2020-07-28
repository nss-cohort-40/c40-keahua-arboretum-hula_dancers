from plants.plant import Plant
from identifiable import Identifiable
from .grassland_plant import GrasslandPlant
from .swamp_plant import SwampPlant


class BlueJadeVine(Plant, Identifiable, GrasslandPlant, SwampPlant):
    def __init__(self):
        Plant.__init__(self)
        Identifiable.__init__(self)
        GrasslandPlant.__init__(self)
        SwampPlant.__init__(self)
        self.sunlight = "partial"
        self.species = "Blue Jade Vine"
