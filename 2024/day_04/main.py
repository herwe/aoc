from enum import Enum


# Top left is origo

class Directions(Enum):
    UP = "UP"
    UP_RIGHT_DIAGONAL = "UP_RIGHT_DIAGONAL"
    VERTICAL_RIGHT = "VERTICAL_RIGHT"
    DOWN_RIGHT_DIAGONAL = "DOWN_RIGHT_DIAGONAL"
    DOWN = "DOWN"
    DOWN_LEFT_DIAGONAL = "DOWN_LEFT_DIAGONAL"
    VERTICAL_LEFT = "VERTICAL_LEFT"
    UP_LEFT_DIAGONAL = "UP_LEFT_DIAGONAL"


def run():
    part_one_and_two()


def part_one_and_two():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    all_coordinates = {}
    only_X_coordinates = {}
    only_A_coordinates = {}

    # Get coordinates
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char == 'X':
                only_X_coordinates[(x, y)] = char
            elif char == 'A':
                only_A_coordinates[(x, y)] = char
            all_coordinates[(x, y)] = char

    part_one_count = 0
    part_two_count = 0
    for x_char_coordinates in only_X_coordinates:
        part_one_count = part_one_count + calculate_based_on_direction(x_char_coordinates, all_coordinates,
                                                                       Directions.UP)
        part_one_count = part_one_count + calculate_based_on_direction(x_char_coordinates, all_coordinates,
                                                                       Directions.UP_RIGHT_DIAGONAL)
        part_one_count = part_one_count + calculate_based_on_direction(x_char_coordinates, all_coordinates,
                                                                       Directions.VERTICAL_RIGHT)
        part_one_count = part_one_count + calculate_based_on_direction(x_char_coordinates, all_coordinates,
                                                                       Directions.DOWN_RIGHT_DIAGONAL)
        part_one_count = part_one_count + calculate_based_on_direction(x_char_coordinates, all_coordinates,
                                                                       Directions.DOWN)
        part_one_count = part_one_count + calculate_based_on_direction(x_char_coordinates, all_coordinates,
                                                                       Directions.DOWN_LEFT_DIAGONAL)
        part_one_count = part_one_count + calculate_based_on_direction(x_char_coordinates, all_coordinates,
                                                                       Directions.VERTICAL_LEFT)
        part_one_count = part_one_count + calculate_based_on_direction(x_char_coordinates, all_coordinates,
                                                                       Directions.UP_LEFT_DIAGONAL)

    for a_char_coordinates in only_A_coordinates:
        part_two_count = part_two_count + calculate_based_on_cross_direction(a_char_coordinates, all_coordinates)

    print(part_one_count)
    print(part_two_count)


def calculate_based_on_direction(x_char_coordinate, all_coordinates, direction) -> int:
    first = all_coordinates[x_char_coordinate]
    x = x_char_coordinate[0]
    y = x_char_coordinate[1]

    if direction == Directions.UP:
        second = all_coordinates[(x, y - 1)]
        third = all_coordinates[(x, y - 2)]
        fourth = all_coordinates[(x, y - 3)]
    elif direction == Directions.UP_RIGHT_DIAGONAL:
        second = all_coordinates[(x + 1, y - 1)]
        third = all_coordinates[(x + 2, y - 2)]
        fourth = all_coordinates[(x + 3, y - 3)]
    elif direction == Directions.VERTICAL_RIGHT:
        second = all_coordinates[(x + 1, y)]
        third = all_coordinates[(x + 2, y)]
        fourth = all_coordinates[(x + 3, y)]
    elif direction == Directions.DOWN_RIGHT_DIAGONAL:
        second = all_coordinates[(x + 1, y + 1)]
        third = all_coordinates[(x + 2, y + 2)]
        fourth = all_coordinates[(x + 3, y + 3)]
    elif direction == Directions.DOWN:
        second = all_coordinates[(x, y + 1)]
        third = all_coordinates[(x, y + 2)]
        fourth = all_coordinates[(x, y + 3)]
    elif direction == Directions.DOWN_LEFT_DIAGONAL:
        second = all_coordinates[(x - 1, y + 1)]
        third = all_coordinates[(x - 2, y + 2)]
        fourth = all_coordinates[(x - 3, y + 3)]
    elif direction == Directions.VERTICAL_LEFT:
        second = all_coordinates[(x - 1, y)]
        third = all_coordinates[(x - 2, y)]
        fourth = all_coordinates[(x - 3, y)]
    elif direction == Directions.UP_LEFT_DIAGONAL:
        second = all_coordinates[(x - 1, y - 1)]
        third = all_coordinates[(x - 2, y - 2)]
        fourth = all_coordinates[(x - 3, y - 3)]

    string = f"{first}{second}{third}{fourth}"

    if string == "XMAS":
        return 1
    return 0


def calculate_based_on_cross_direction(a_char_coordinate, all_coordinates) -> int:
    first = all_coordinates[a_char_coordinate]
    x = a_char_coordinate[0]
    y = a_char_coordinate[1]

    up_right = all_coordinates[(x + 1, y - 1)]
    up_left = all_coordinates[(x - 1, y - 1)]
    down_right = all_coordinates[(x + 1, y + 1)]
    down_left = all_coordinates[(x - 1, y + 1)]

    string = f"{up_right}{up_left}{down_right}{down_left}"

    # There is one case we need to check for, even if the counts are correct.
    sub1 = f"{up_right}{first}{down_left}"
    sub2 = f"{up_left}{first}{down_right}"

    count_S = string.count("S")
    count_M = string.count("M")

    if count_S == 2 and count_M == 2 and sub1 != ("SAS" or "MAM") and sub2 != ("SAS" or "MAM"):
        return 1
    return 0


if __name__ == "__main__":
    run()
