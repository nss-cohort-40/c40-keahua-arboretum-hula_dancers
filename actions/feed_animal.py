from animals.river_dolphin import RiverDolphin
from animals.pueo import Pueo
from animals.ulae import Ulae
from animals.gold_dust_day_gecko import Gold_dust_day_gecko
from animals.nene_goose import Nene_goose
from animals.kikakapu import Kikakapu
from animals.opeapea import Opeapea
from animals.hawaiian_happyface_spider import Hawaiian_happyface_spider


def feed_animal(arboretum):
    animal = None

    print("1. River Dolphin")
    print("2. Pueo")
    print("3. Ulae")
    print("4. Gold Dust Day Gecko")
    print("5. Nene Goose")
    print("6. Kikakapu")
    print("7. Ope'ape'a")
    print("8. Hawaiian Happy-Face Spider")

    choice = input("Choose an animal to feed > ")

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

    animal.feed(animal)
