def build_facility_report(arboretum):
    for river in arboretum.rivers:
        print(f'{river.name} - {river.id}')
        for animal in river.animals:
            print(f'ANIMAL: {animal.species} - {animal.id}')
        print(
            f"  *{river.name} has {len(river.animals)} animals and {len(river.plants)} plants in it")

    for swamp in arboretum.swamps:
        print(f'{swamp.name} - {swamp.id}]')
        print(
            f"  *{swamp.name} has {len(swamp.animals)} animals and {len(swamp.plants)} plants in it")

    input("\n\nPress any key to continue...")
