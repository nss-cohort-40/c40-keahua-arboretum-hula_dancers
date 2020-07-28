from animals.river_dolphin import RiverDolphin
from animals.pueo import Pueo
from animals.ulae import Ulae
from animals.gold_dust_day_gecko import Gold_dust_day_gecko
from animals.nene_goose import Nene_goose
from animals.kikakapu import Kikakapu
from animals.opeapea import Opeapea
from animals.hawaiian_happyface_spider import Hawaiian_happyface_spider


def feed_animal(arboretum):

    print("1. River Dolphin")
    print("2. Pueo")
    print("3. Ulae")
    print("4. Gold Dust Day Gecko")
    print("5. Nene Goose")
    print("6. Kikakapu")
    print("7. Ope'ape'a")
    print("8. Hawaiian Happy-Face Spider")

    choice = input("Choose an animal to feed > ")

    def chosenAnimal(animal):
        for index, prey in enumerate(animal.prey):
            print(f"{index + 1}. {prey}")

        choice_of_prey = input(
            f"\nWhat's on the menu for the {animal.species} today? \n> ")

        input(
            f"\n>>> The {animal.species} devoured the {animal.prey[int(choice_of_prey) - 1].lower()} <<<\n\nPress enter to return to the main menu.")

    if choice == "1":
        chosenAnimal(RiverDolphin())
    if choice == "2":
        chosenAnimal(Pueo())
    if choice == "3":
        chosenAnimal(Ulae())
    if choice == "4":
        chosenAnimal(Gold_dust_day_gecko())
    if choice == "5":
        chosenAnimal(Nene_Goose())
    if choice == "6":
        chosenAnimal(Kikakapu())
    if choice == "7":
        chosenAnimal(Opeapea())
    if choice == "8":
        chosenAnimal(Hawaiian_happyface_spider())
