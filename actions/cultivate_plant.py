from plants import MountainAppleTree
from plants import Silversword
from plants import RainbowEucalyptusTree
from plants import BlueJadeVine


def cultivate_plant(arboretum):
    plant = None

    print("\nChoose plant to cultivate.")
    print("\n\n1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")

    choice = input(">_")

    if choice == "1":
        plant = MountainAppleTree()
        plant

    if choice == "2":
        plant = Silversword()

    if choice == "3":
        plant = RainbowEucalyptusTree()

    if choice == "4":
        plant = BlueJadeVine()
