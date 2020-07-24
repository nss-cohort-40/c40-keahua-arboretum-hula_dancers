def build_facility_report(arboretum):
    for river in arboretum.rivers:
        print(f'{river.name} - {river.id}')
        print(f"This place has {len(river.animals)} animals in it")

    for swamp in arboretum.swamps:
        swamp_id = str(swamp.id)
        print(swamp_id)
        print(f'{swamp.name} - {swamp_id[:9]}')

    for coastline in arboretum.coastlines:
        print(f'{coastline.name} - {coastline.id}]')

    for grassland in arboretum.grasslands:
        print(f'{grassland.name} - {grassland.id}]')

    for forest in arboretum.forests:
        print(f'{forest.name} - {forest.id}]')

    for mountain in arboretum.mountains:
        print(f'{mountain.name} - {mountain.id}]')

    input("\n\nPress any key to continue...")
