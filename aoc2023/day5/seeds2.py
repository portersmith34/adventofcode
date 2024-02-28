def find_first_location(file):
    maps = []
    location_list = []
    blocks = file.split("\n\n")
    seed_list = [int(x) for x in blocks[0].split()[1:]] 
    
    # create maps
    for section in blocks[1:]:
        new_map = SeedMap()
        for line in section.split("\n")[1:]:
            dest, source, length = [int(x) for x in line.split()]
            new_map.dict[(source, source+length)] = dest
        maps.append(new_map)
    
    # do the mapping
    for seed in seed_list:
        for current_map in maps:
            seed = current_map.process(seed)
        location_list.append(seed)
    return min(location_list)

class SeedMap:
    
    def __init__(self):
        self.dict = {}
    
    def process(self, input_number):
        for input_range in self.dict:
            if input_number in range(input_range[0], input_range[1]):
                output_number = (input_number - input_range[0]) + self.dict[(input_range[0], input_range[1])]
                return output_number
        
        return input_number
