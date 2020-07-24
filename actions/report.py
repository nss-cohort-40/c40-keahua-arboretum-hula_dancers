def build_facility_report(arboretum):
    for river in arboretum.rivers:
        print(f'{river.name} - {river.id}')
        print(f"This place has {len(river.animals)} animals in it")

    for swamp in arboretum.swamps:
        print(f'{swamp.name} - {swamp.id}]')

    for coastline in arboretum.coastlines:
        print(f'{coastline.name} - {coastline.id}]')

    input("\n\nPress any key to continue...")
