import os
from plants import MountainAppleTree
from plants import Silversword
from plants import RainbowEucalyptusTree
from plants import BlueJadeVine


def cultivate_plant(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    plant = None

    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")

    print("\nChoose plant to cultivate.")
    choice = input(">_ ")

    if choice == "1":
        plant = MountainAppleTree()
    print(f'Where you would you like to plant this {plant.species}')

    if choice == "2":
        plant = Silversword()

    if choice == "3":
        plant = RainbowEucalyptusTree()

    if choice == "4":
        plant = BlueJadeVine()
