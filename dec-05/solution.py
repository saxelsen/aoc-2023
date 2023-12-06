from collections import defaultdict
import re
import itertools


def num_in_range(num: int, _range: tuple[int, int]) -> bool:
    return _range[0] <= num < _range[1]


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    seeds = [int(seed) for seed in lines[0].split(":")[1].split()]
    seed_ranges = [(start, start + end) for start, end in zip(seeds[::2], seeds[1::2])]

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
    lowest_seed = None
    for seed in seeds:
        new_val = seed
        for map_name, maps in mappings.items():
            for map in maps:
                if map["src"] <= new_val < map["src"] + map["range"]:
                    new_val = map["dest"] + (new_val - map["src"])
                    break
        if lowest is None or new_val < lowest:
            lowest = new_val
            lowest_seed = seed

    print(lowest)
    print(lowest_seed)

    print("Reversing")
    reversed_maps = list(reversed(mappings.items()))
    finished = False

    for i in itertools.count(start=1):
        if i % 1_000_000 == 0:
            print(i)
        mapped_val = i
        for map_name, maps in reversed_maps:
            for map in maps:
                if map["dest"] <= mapped_val < map["dest"] + map["range"]:
                    mapped_val = map["src"] + (mapped_val - map["dest"])
                    break
        for _range in seed_ranges:
            if _range[0] <= mapped_val < _range[1]:
                print(f"{i} in range {_range}")
                finished = True
                break

        if finished:
            break
