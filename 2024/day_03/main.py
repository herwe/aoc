import re


def run():
    part_one()
    part_two()


def part_one():
    pattern = r"mul\((-?\d+),\s*(-?\d+)\)"
    with open("input.txt", "r") as f:
        lines = f.read()

    muls = re.findall(pattern, lines)
    result = sum([(int(x) * int(y)) for x, y in muls])
    print(result)



def part_two():
    """
    Find occurrences of 'mul(x, y)' and 'do' and 'don'
    Get positions of the elements (first character)
    Put in a map with key position and value the pattern string
    Merge all maps together and sort
    Go through each key and figure out what muls should be included in the final sum, add to list
    Remove prefix 'mul', convert to tuple and sum

    Probably could have dealt with the prefix earlier??IDK:)
    """

    muls_pattern = r"mul\((-?\d+),\s*(-?\d+)\)"
    donts_pattern = r"\bdon\b"
    do_pattern = r"\bdo\b"
    with open("input.txt", "r") as f:
        lines = f.read()

    donts_matches = re.finditer(donts_pattern, lines)
    donts_map = {match.start(): match.group() for match in donts_matches}

    do_matches = re.finditer(do_pattern, lines)
    do_map = {match.start(): match.group() for match in do_matches}

    muls_matches = re.finditer(muls_pattern, lines)
    muls_map = {match.start(): match.group() for match in muls_matches}

    merged_map = {**donts_map, **do_map, **muls_map}
    ordered_map = dict(sorted(merged_map.items()))

    dont_cycle = False
    valid_muls = []
    for position in ordered_map:
        value = ordered_map[position]
        if value.startswith("don"):
            dont_cycle = True
            continue
        if value.startswith("do") and not value.startswith("don"):
            dont_cycle = False
            continue
        if dont_cycle is False:
            valid_muls.append(value)

    muls_as_tuples = [tuple(re.search(r"mul\((\d+),(\d+)\)", mul).groups()) for mul in valid_muls]
    result = sum([(int(x) * int(y)) for x, y in muls_as_tuples])
    print(result)


if __name__ == "__main__":
    run()
