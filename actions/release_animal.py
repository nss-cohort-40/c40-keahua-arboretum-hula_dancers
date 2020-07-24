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
        rivers_and_swamps = arboretum.rivers + arboretum.swamps
        print(rivers_and_swamps)
        for index, river_swamp in enumerate(rivers_and_swamps):
            print(f'{index + 1}. River/Swamp: {river_swamp.name} - {river_swamp.id}')
            print("Release the animal into which biome?")
            choice = input("> ")

        arboretum.rivers[int(choice) - 1].animals.append(animal)


    if choice == "2":
        pass
        



