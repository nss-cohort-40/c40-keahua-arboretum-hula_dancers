import os
from environments.river import River
from environments.swamp import Swamp
from environments.coastline import Coastline
from environments.grassland import Grassland
from environments.forest import Forest
from environments.mountain import Mountain


def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')

    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Forest")
    print("6. Mountain")

    choice = input("Choose your habitat > ")
    name = input("Please choose a habitat's name > ")
# DONE - add name property to habitats so people can read that stuff
    if choice == "1":
        river = River(name)
        arboretum.selected_biome = "river"
        arboretum.rivers.append(river)
        arboretum.biome_type = river
    if choice == "2":
        swamp = Swamp(name)
        arboretum.swamps.append(swamp)
    if choice == "3":
        coastline = Coastline(name)
        arboretum.coastlines.append(coastline)
    if choice == "4":
        grassland = Grassland(name)
        arboretum.grasslands.append(grassland)
    if choice == "5":
        forest = Forest(name)
        arboretum.forests.append(forest)
    if choice == "6":
        mountain = Mountain(name)
        arboretum.mountains.append(mountain)
