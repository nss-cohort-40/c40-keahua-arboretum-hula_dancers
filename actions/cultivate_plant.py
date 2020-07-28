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

    print(f'\n- * C U L T I V A T E * -\n')
    all_biomes = arboretum.mountains + arboretum.grasslands + arboretum.swamps + \
        arboretum.forests + arboretum.rivers + arboretum.coastlines
    for index, biome in enumerate(all_biomes):
        print(
            f'{index + 1}. {biome.name} {biome.biome_type} ({len(biome.plants)} plants)')
    print(f"Which biome would you like to cultivate your {plant.species} in?")
    biome_selection = input("> ")
    biome_to_append = all_biomes[int(biome_selection) - 1]
    biome_to_append.plant_max_capacity(plant)
