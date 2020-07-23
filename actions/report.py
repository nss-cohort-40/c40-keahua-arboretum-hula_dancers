def build_facility_report(arboretum):
    for river in arboretum.rivers:
        print(f'River [{river.id}]')

    for swamp in arboretum.swamps:
        print(f'Swamp [{swamp.id}]')

    input("\n\nPress any key to continue...")
