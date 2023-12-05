from collections import defaultdict
import re

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    seeds = [int(seed) for seed in lines[0].split(":")[1].split()]

    parsers = defaultdict(bool)
    mappings = defaultdict(list)
    current_map = ""
    for line in lines[1:]:
        if mapping_match := re.match(r"(\w+-to-\w+)", line):
            current_map = mapping_match.group(1)

        if line != "" and re.match(r"\d", line):
            dest, source, ran = line.split()
            mappings[current_map].append({"dest": int(dest), "src": int(source), "range": int(ran)})

    lowest = None
    for seed in seeds:
        new_val = seed
        for map_name, maps in mappings.items():
            mapped = False
            for map in maps:
                if map["src"] <= new_val < map["src"] + map["range"]:
                    new_val = map["dest"] + (new_val - map["src"])
                    mapped = True
                    break
        if lowest is None:
            lowest = new_val
        elif new_val < lowest:
            lowest = new_val

    print(lowest)
