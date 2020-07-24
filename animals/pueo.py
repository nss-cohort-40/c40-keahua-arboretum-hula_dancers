from animals.animal import Animal
from identifiable import Identifiable
# from evironments.grassland import Grassland
# from environments.forest import Forest

class Pueo(Animal, Identifiable): #add Freshwater

    def __init__(self):
        # Animal.__init__(self, "Pueo")
        # Grassland.__init__(self)
        # Forest.__init__(self)
        Identifiable.__init__(self)
        Animal.prey = {}
        

        


