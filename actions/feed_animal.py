

def feed_animal(arboretum):

    print("1. River Dolphin")
    print("2. Pueo")
    print("3. Ulae")
    print("4. Gold Dust Day Gecko")
    print("5. Nene Goose")
    print("6. Kikakapu")
    print("7. Ope'ape'a")
    print("8. Hawaiian Happy-Face Spider")

    choice = input("Choose an animal to feed > ")

    def chosenAnimal(animal, arr):
        for index, prey in arr.prey:
            print(f"{index + 1}. {prey}")

        choice_of_prey = input(
            f"What's on the menu for the {animal} today? \n> ")

        input(
            f"The {animal} gobbled it up.\nPress enter to return to the main menu.")

    if choice == "1":
        chosenAnimal("river dolphin")
    if choice == "2":
        chosenAnimal("pueo")
    if choice == "3":
        chosenAnimal("ulae")
    if choice == "4":
        chosenAnimal("gold dust day gecko")
    if choice == "5":
        chosenAnimal("nene goose")
    if choice == "6":
        chosenAnimal("kikakapu")
    if choice == "7":
        chosenAnimal("ope'ape'a")
    if choice == "8":
        chosenAnimal("Hawaiin happy face spider")
