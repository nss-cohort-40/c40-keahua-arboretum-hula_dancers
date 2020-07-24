

class Animal:

    def __init__(self, species):
        self.species = species
        self.age_in_months = 0
        self.minimum_age_in_months = 0
        self.__prey = {}

    def move(self, propulsion, speed):
        return f"{self.species} moves at {speed} meters/sec by {propulsion}"

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The {self.species} ate {prey} for a meal')
