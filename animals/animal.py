

class Animal:

    def __init__(self, species):
        self.species = species
        self.age_in_months = 0
        self.minimum_age_in_months = 0
        self.__prey = []

    def move(self, propulsion, speed):
        return f"{self.species} moves at {speed} meters/sec by {propulsion}"

    @property
    def prey(self):
        return self.__prey

    def feed(self, animal):
        for index, prey in enumerate(animal.prey):
            print(f"{index + 1}. {prey}")

        choice_of_prey = input(
            f"\nWhat's on the menu for the {animal.species} today? \n> ")

        input(
            f"\n>>> The {animal.species.lower()} devoured the {animal.prey[int(choice_of_prey) - 1].lower()} <<<\n\nPress enter to return to the main menu.")
