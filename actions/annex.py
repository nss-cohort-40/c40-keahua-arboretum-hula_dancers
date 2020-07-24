import os
from environments.river import River
from environments.swamp import Swamp


def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')

    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")

    choice = input("Choose your habitat > ")
    name = input("Please choose a habitat's name > ")
# DONE - add name property to habitats so people can read that stuff
    if choice == "1":
        river = River(name)
        arboretum.selected_biome = "river"
        arboretum.rivers.append(river)
    if choice == "2":
        swamp = Swamp(name)
        arboretum.selected_biome = swamp
        arboretum.swamps.append(swamp)