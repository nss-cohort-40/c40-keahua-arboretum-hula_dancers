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

    if choice == "2":
        animal = Pueo()

    if choice == "3":
        animal = Ulae()

    if choice == "4":
        animal = Gold_dust_day_gecko()

    if choice == "5":
        animal = Nene_goose()

    if choice == "6":
        animal = Kikakapu()
   
    if choice == "7":
        animal = Opeapea()

    if choice == "8":
        animal = Hawaiian_happyface_spider()

    all_biomes = arboretum.rivers + arboretum.forests + arboretum.coastlines + \
        arboretum.swamps + arboretum.grasslands + arboretum.mountains
    animal_age_in_months = input("Enter animal age in months > ")
    animal_age_float = float(animal_age_in_months)
    if animal_age_float < animal.minimum_age_in_months:
        print("\n\nAnimal is too young to be released. Please choose a older animal.")
        input("\n\nPress any key to continue...")
        release_animal(arboretum)
    else:
        for index, biome in enumerate(all_biomes):
            print(
                f'{index + 1}. {biome.name} {biome.biome_type} ({len(biome.animals)} animals)')
        print("Release the animal into which biome?")
        biome_selection = input("> ")
        all_biomes[int(biome_selection) - 1].add_animal(animal)

