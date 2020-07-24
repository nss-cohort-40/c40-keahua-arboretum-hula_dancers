

def cultivate_plant(arboretum):
    plant = None

    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")

    print("Choose plant to cultivate.")
    choice = input(">_")

    if choice == "1":
        plant = MountainAppleTree()

    if choice == "2":
        plant = Silversword()

    if choice == "3":
        plant = RainbowEucalyptusTree()

    if choice == "4":
        plant = BlueJadeVine()
