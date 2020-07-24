def build_facility_report(arboretum):
    for river in arboretum.rivers:
        river_id = str(river.id)
        print(f'{river.name} - {river_id[:8]}')
        print(f"This place has {len(river.animals)} animals in it")

    for swamp in arboretum.swamps:
        swamp_id = str(swamp.id)
        print(f'{swamp.name} - {swamp_id[:8]}')
        print(f"This place has {len(swamp.animals)} animals in it")

    for coastline in arboretum.coastlines:
        coastline_id = str(coastline.id)
        print(f'{coastline.name} - {coastline_id[:8]}]')
        print(f"This place has {len(coastline.animals)} animals in it")

    for grassland in arboretum.grasslands:
        grassland_id = str(grassland.id)
        print(f'{grassland.name} - {grassland_id[:8]}]')
        print(f"This place has {len(grassland.animals)} animals in it")

    for forest in arboretum.forests:
        forest_id = str(forest.id)
        print(f'{forest.name} - {forest_id[:8]}]')
        print(f"This place has {len(forest.animals)} animals in it")

    for mountain in arboretum.mountains:
        mountain_id = str(mountain.id)
        print(f'{mountain.name} - {mountain_id[:8]}]')
        print(f"This place has {len(mountain.animals)} animals in it")

    input("\n\nPress any key to continue...")
