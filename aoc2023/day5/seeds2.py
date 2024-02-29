
def find_first_location(file):
    maps = []
    blocks = file.split("\n\n")
    seed_list = [int(x) for x in blocks[0].split()[1:]] 
    seed_list = list(zip(seed_list[::2], seed_list[1::2]))
    
    # create maps
    for section in blocks[1:]:
        new_map = []
        for line in section.split("\n")[1:]:
            dest, source, length = [int(x) for x in line.split()]
            new_map.append((source, source+length, dest))
        maps.append(new_map)
    
    # TODO: do transformations on the seed range list instead of on the individual seeds
    for current_map in maps:
        i = 0
        while i < len(seed_list):
            for map_in_start, map_in_end, map_out_start in current_map: 
                start_seed, dist = seed_list[i]
                end_seed = start_seed + dist
                if start_seed in range(map_in_start, map_in_end) and end_seed in range(map_in_start, map_in_end):
                    dist_from_map = start_seed - map_in_start
                    start_seed = dist_from_map + map_out_start
                    seed_list[i] = (start_seed, dist)
                # end extends past the new map
                elif start_seed in range(map_in_start, map_in_end) and not end_seed in range(map_in_start, map_in_end):
                    dist_from_map = start_seed - map_in_start
                    start_seed = dist_from_map + map_out_start
                    old_dist = dist
                    dist = map_in_end - map_in_start - dist_from_map  
                    new_dist =  old_dist - dist
                    new_start_seed = end_seed - new_dist
                    seed_list[i] = (start_seed, dist)
                    seed_list.append((new_start_seed, new_dist))
                # start is before new map
                elif end_seed in range(map_in_start, map_in_end) and not start_seed in range(map_in_start, map_in_end):
                    new_start_seed = start_seed
                    start_seed = map_out_start
                    old_dist = dist
                    dist = map_in_start - new_start_seed 
                    new_dist = old_dist - dist
                    seed_list[i] = (start_seed, dist)
                    seed_list.append((new_start_seed, new_dist))
            i += 1
    seed_list.sort()
    return(seed_list[0][0])



with open("aoc2023/day5/test input.txt", "r") as file:
    sample = file.read()
print(find_first_location(sample))