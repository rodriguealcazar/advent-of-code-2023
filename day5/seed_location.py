import sys


def _ordered_mappings(lines):
    mappings = []
    while mapping := lines.pop(0):
        to_, from_, range_ = mapping.split(" ")
        mappings.append((int(from_), int(to_), int(range_)))
    return sorted(mappings, key=lambda t: t[0])


def main(lines):
    seeds = [int(s) for s in lines.pop(0).split("seeds: ")[1].split(" ")]
    lines.pop(0)  # Empty line

    seeds_to_locations = []

    maps = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]
    for map in maps:
        if lines[0] != f"{map} map:":
            raise RuntimeError(f"Expected {map}: {lines[0]}")
        lines.pop(0)  # Header
        seeds_to_locations.append(_ordered_mappings(lines))

    min_location = None
    for seed in seeds:
        for map in seeds_to_locations:
            for mapping in map:
                if seed < mapping[0]:
                    break
                if mapping[0] <= seed < mapping[0] + mapping[2]:
                    seed += mapping[1] - mapping[0]
                    break
        if min_location is None or seed < min_location:
            min_location = seed
    print(min_location)


if __name__ == "__main__":
    file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    with open(file, "r") as f:
        main(f.read().splitlines())
