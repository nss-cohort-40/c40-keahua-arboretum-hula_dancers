from animals.river_dolphin import RiverDolphin
# from animals.Pueo import Pueo


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
        animal_age_int = int(animal_age_in_months)
        if animal_age_int < animal.minimum_age_in_months:
            print("\n\nAnimal is too young to be released. Please choose a older animal.")
            input("\n\nPress any key to continue...")
            release_animal(arboretum)
            #return to release_animal menu
        else:
            rivers_and_swamps = arboretum.rivers + arboretum.swamps
            for index, river_swamp in enumerate(rivers_and_swamps):
                print(f'{index + 1}. River/Swamp: {river_swamp.name} - {river_swamp.id}')
            print("Release the animal into which biome?")
            choice = input("> ")
            rivers_and_swamps[int(choice) - 1].animals.append(animal)

    if choice == "2":
        pass


        



