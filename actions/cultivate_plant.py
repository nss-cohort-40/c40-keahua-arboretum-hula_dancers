import os
from plants.mountain_apple_tree import MountainAppleTree
from plants.silversword import Silversword
from plants.rainbow_eucalyptus_tree import RainbowEucalyptusTree
from plants.blue_jade_vine import BlueJadeVine


def cultivate_plant(arboretum):
    # os.system('cls' if os.name == 'nt' else 'clear')
    plant = None

    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")

    plant_selection = input("\nChoose plant to cultivate > ")

    if plant_selection == "1":
        plant = MountainAppleTree()

    if plant_selection == "2":
        plant = Silversword()

    if plant_selection == "3":
        plant = RainbowEucalyptusTree()

    if plant_selection == "4":
        plant = BlueJadeVine()

    print(f'Where you would you like to plant this {plant.species}?')
    mountains = arboretum.mountains
    for index, mountain in enumerate(mountains):
        if len(mountains) > 0:
            print(f'{index + 1}. {mountain.name} {mountain.biome_type}')
        else:
            input(
                "\n**There are currently no available mountain biomes to cultivate this plant in. ")
    input("\n\nPress any key to continue...")
