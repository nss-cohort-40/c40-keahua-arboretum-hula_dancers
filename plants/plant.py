from identifiable import Identifiable


class Plant(Identifiable):

    def __init__(self):
        super().__init__()
        self.species = ''
        # self.peak_season = season
        self.sunlight = ''
