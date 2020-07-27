from .aquatic import Aquatic

class Freshwater(Aquatic):

    def __init__(self):
        super().__init__()
        self.exists_in_freshwater = True
