from plants import Plant
from identifiable import Identifiable


class Silversword(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self)
        Identifiable.__init__(self)
        self.sunlight = "full"
