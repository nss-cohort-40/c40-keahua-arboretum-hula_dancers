def build_facility_report(arboretum):
    all_biomes = arboretum.rivers + arboretum.forests + arboretum.coastlines + \
        arboretum.swamps + arboretum.grasslands + arboretum.mountains
    for biome in all_biomes:
        biome_id = str(biome.id)
        all_organisms = biome.animals + biome.plants
        print(f'{biome.name} {biome.biome_type} - {biome_id[:8]}')
        for organism in all_organisms:
            organism_id = str(organism.id)
            print(f'    {organism.species} ({organism_id[:8]})')
    input("\n\nPress any key to continue...")
