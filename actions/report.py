def build_facility_report(arboretum):
    all_biomes = arboretum.rivers + arboretum.forests + arboretum.coastlines + \
        arboretum.swamps + arboretum.grasslands + arboretum.mountains
    for biome in all_biomes:
        biome_id = str(biome.id)
        print(f'{biome.name} - {biome_id[:8]}')
        print(f"There are {len(biome.animals)} animals here.")
    input("\n\nPress any key to continue...")
