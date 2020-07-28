from .aquatic import Aquatic

class Saltwater(Aquatic):

    def __init__(self):
        super().__init__()
        self.exists_in_saltwater = True
