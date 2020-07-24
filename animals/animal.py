# 1. build a function that doesn't allow an animal to be released into the wild before their recommended release age
# Pueo MINIMUM RELEASE AGE 8 months
# River Dolphins MINIMUM RELEASE AGE 13 months
# 'Ulae MINIMUM RELEASE AGE 1 months
# Gold Dust Day Gecko MINIMUM RELEASE AGE 2 months
# Nene Goose MINIMUM RELEASE AGE 7 months
# Kikakapu MINIMUM RELEASE AGE 1 months
# Ope'ape'a MINIMUM RELEASE AGE 5 months
# Hawaiian Happy-Face Spider MINIMUM RELEASE AGE 0.5 months

# 2. Animals should not be fed anything other than their recomended prey
# Pueo RECOMMENDED PREY Rodents
# River Dolphins RECOMMENDED PREY Fish
# 'Ulae RECOMMENDED PREY Fish
# Gold Dust Day Gecko RECOMMENDED PREY Insects
# Nene Goose RECOMMENDED PREY Vegetation
# Kikakapu RECOMMENDED PREY Fish
# Ope'ape'a RECOMMENDED PREY Insects & Vegetation
# Hawaiian Happy-Face Spider RECOMMENDED PREY Insects

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
