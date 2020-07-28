def build_facility_report(arboretum):
    for river in arboretum.rivers:
        river_id = str(river.id)
        print(f'{river.name} - {river_id[:8]}')
        print(f"There are {len(river.animals)} animals here.")

    for swamp in arboretum.swamps:
        swamp_id = str(swamp.id)
        swamp_inhabitants = swamp.animals + swamp.plants
        print(f'{swamp.name} - {swamp_id[:8]}')
        # print(f"There are {len(swamp.animals)} animals here.")
        for inhabitant in swamp_inhabitants:
            print(f'    {inhabitant.species}')

    for coastline in arboretum.coastlines:
        coastline_id = str(coastline.id)
        print(f'{coastline.name} - {coastline_id[:8]}')
        print(f"There are {len(coastline.animals)} animals here.")

    for grassland in arboretum.grasslands:
        grassland_id = str(grassland.id)
        print(f'{grassland.name} - {grassland_id[:8]}')
        print(f"There are {len(grassland.animals)} animals here.")

    for forest in arboretum.forests:
        forest_id = str(forest.id)
        print(f'{forest.name} - {forest_id[:8]}')
        print(f"There are {len(forest.animals)} animals here.")

    for mountain in arboretum.mountains:
        mountain_id = str(mountain.id)
        print(f'{mountain.name} - {mountain_id[:8]}')
        print(f"There are {len(mountain.animals)} animals here.")

    input("\n\nPress any key to continue...")
