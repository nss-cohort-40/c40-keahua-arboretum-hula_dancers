from animals.pueo import Pueo
from animals.river_dolphin import RiverDolphin
from animals.ulae import Ulae
from animals.gold_dust_day_gecko import Gold_dust_day_gecko
from animals.nene_goose import Nene_goose
from animals.kikakapu import Kikakapu
from animals.opeapea import Opeapea
from animals.hawaiian_happyface_spider import Hawaiian_happyface_spider


def release_animal(arboretum):
    animal = None

    print("1. River Dolphins")
    print("2. Pueo")
    print("3. \'Ulae")
    print("4. Gold Dust Day Gecko")
    print("5. Nene Goose")
    print("6. Kikakapu")
    print("7. Ope\'ape\'a")
    print("8. Hawaiian Happy-Face Spider")

    choice = input("Choose animal to release > ")



    if choice == "1":
        animal = RiverDolphin()
        animal_age_in_months = input("Enter animal age in months > ")
        animal_age_float = float(animal_age_in_months)
        if animal_age_float < animal.minimum_age_in_months:
            print("\n\nAnimal is too young to be released. Please choose a older animal.")
            input("\n\nPress any key to continue...")
            release_animal(arboretum)
        else:
            rivers_and_swamps = arboretum.rivers + arboretum.swamps
            for index, river_swamp in enumerate(rivers_and_swamps):
                print(f'{index + 1}. {river_swamp.name} {river_swamp.biome_type} ({len(river_swamp.animals)} animals)')
            print("Release the animal into which biome?")
            choice = input("> ")
            rivers_and_swamps[int(choice) - 1].animals.append(animal)

    if choice == "2":
        animal = Pueo()
        animal_age_in_months = input("Enter animal age in months > ")
        animal_age_float = float(animal_age_in_months)
        if animal_age_float < animal.minimum_age_in_months:
            print("\n\nAnimal is too young to be released. Please choose a older animal.")
            input("\n\nPress any key to continue...")
            release_animal(arboretum)
            # return to release_animal menu
        else:
            # TODO: Display all of the locations in which the animals can be stored.
            # TODO: Display The current number of animals
            pass

    if choice == "3":
        animal = Ulae()
        animal_age_in_months = input("Enter animal age in months > ")
        animal_age_float = float(animal_age_in_months)
        if animal_age_float < animal.minimum_age_in_months:
            print("\n\nAnimal is too young to be released. Please choose a older animal.")
            input("\n\nPress any key to continue...")
            release_animal(arboretum)
            # return to release_animal menu
        else:
            # TODO: Display all of the locations in which the animals can be stored.
            # TODO: Display The current number of animals
            pass
    if choice == "4":
        animal = Gold_dust_day_gecko()
        animal_age_in_months = input("Enter animal age in months > ")
        animal_age_float = float(animal_age_in_months)
        if animal_age_float < animal.minimum_age_in_months:
            print("\n\nAnimal is too young to be released. Please choose a older animal.")
            input("\n\nPress any key to continue...")
            release_animal(arboretum)
            # return to release_animal menu
        else:
            # TODO: Display all of the locations in which the animals can be stored.
            # TODO: Display The current number of animals
            pass

    if choice == "5":
        animal = Nene_goose()
        animal_age_in_months = input("Enter animal age in months > ")
        animal_age_float = float(animal_age_in_months)
        if animal_age_float < animal.minimum_age_in_months:
            print("\n\nAnimal is too young to be released. Please choose a older animal.")
            input("\n\nPress any key to continue...")
            release_animal(arboretum)
            # return to release_animal menu
        else:
            # TODO: Display all of the locations in which the animals can be stored.
            # TODO: Display The current number of animals
            pass

    if choice == "6":
        animal = Kikakapu()
        animal_age_in_months = input("Enter animal age in months > ")
        animal_age_float = float(animal_age_in_months)
        if animal_age_float < animal.minimum_age_in_months:
            print("\n\nAnimal is too young to be released. Please choose a older animal.")
            input("\n\nPress any key to continue...")
            release_animal(arboretum)
            # return to release_animal menu
        else:
            # TODO: Display all of the locations in which the animals can be stored.
            # TODO: Display The current number of animals
            pass

    if choice == "7":
        animal = Opeapea()
        animal_age_in_months = input("Enter animal age in months > ")
        animal_age_float = float(animal_age_in_months)
        if animal_age_float < animal.minimum_age_in_months:
            print("\n\nAnimal is too young to be released. Please choose a older animal.")
            input("\n\nPress any key to continue...")
            release_animal(arboretum)
            # return to release_animal menu
        else:
            # TODO: Display all of the locations in which the animals can be stored.
            # TODO: Display The current number of animals
            pass

    if choice == "8":
        animal = Kikakapu()
        animal_age_in_months = input("Enter animal age in months > ")
        animal_age_float = float(animal_age_in_months)
        if animal_age_float < animal.minimum_age_in_months:
            print("\n\nAnimal is too young to be released. Please choose a older animal.")
            input("\n\nPress any key to continue...")
            release_animal(arboretum)
            # return to release_animal menu
        else:
            # TODO: Display all of the locations in which the animals can be stored.
            # TODO: Display The current number of animals
            pass
