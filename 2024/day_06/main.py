from enum import Enum


# Direction guard is facing
class Direction(Enum):
    UP = "UP"
    RIGHT = "RIGHT"
    DOWN = "DOWN"
    LEFT = "LEFT"


class Guard:
    def __init__(self):
        self.direction = None
        self.pos = None

    def __int__(self, direction, pos):
        self.direction = direction
        self.pos = pos

    def turn_right(self):
        if self.direction == Direction.UP:
            self.direction = Direction.RIGHT
        elif self.direction == Direction.RIGHT:
            self.direction = Direction.DOWN
        elif self.direction == Direction.DOWN:
            self.direction = Direction.LEFT
        elif self.direction == Direction.LEFT:
            self.direction = Direction.UP


def part_one():
    all_coordinates = {}
    visited_positions = set()
    guard = None
    with open("input.txt", "r") as f:
        lines = f.readlines()

    # Get coordinates
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char == '^':
                guard = Guard()
                guard.direction = Direction.UP
                guard.pos = (x, y)
                visited_positions.add((x, y))
            all_coordinates[(x, y)] = char

    while True:
        x = guard.pos[0]
        y = guard.pos[1]
        if guard.direction == Direction.UP:
            if y - 1 < 0:
                break
        elif guard.direction == Direction.RIGHT:
            if x + 1 > 129:
                break
        elif guard.direction == Direction.DOWN:
            if y + 1 > 129:
                break
        elif guard.direction == Direction.LEFT:
            if x - 1 < 0:
                break

        if guard.direction == Direction.UP:
            if all_coordinates[(x, y - 1)] == "#":
                guard.turn_right()
            else:
                guard.pos = (x, y - 1)
            visited_positions.add(guard.pos)
        elif guard.direction == Direction.RIGHT:
            if all_coordinates[(x + 1, y)] == "#":
                guard.turn_right()
            else:
                guard.pos = (x + 1, y)
            visited_positions.add(guard.pos)
        elif guard.direction == Direction.DOWN:
            if all_coordinates[(x, y + 1)] == "#":
                guard.turn_right()
            else:
                guard.pos = (x, y + 1)
            visited_positions.add(guard.pos)
        elif guard.direction == Direction.LEFT:
            if all_coordinates[(x - 1, y)] == "#":
                guard.turn_right()
            else:
                guard.pos = (x - 1, y)
            visited_positions.add(guard.pos)

    print(len(visited_positions))


def part_two():
    all_coordinates = {}
    visited_positions = set()
    obstruction_count = 0
    guard = None
    start = None
    with open("input.txt", "r") as f:
        lines = f.readlines()

    # Get coordinates
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char == '^':
                guard = Guard()
                guard.direction = Direction.UP
                guard.pos = (x, y)
                start = (x, y, Direction.UP)
                visited_positions.add(start)
            all_coordinates[(x, y)] = char

    for coordPair in all_coordinates:
        if all_coordinates[coordPair] == '#' or all_coordinates[coordPair] == '^':
            continue

        all_coordinates[coordPair] = '#'

        visited_positions.clear()
        visited_positions.add(start)
        pos = (start[0], start[1])
        guard.pos = pos
        guard.direction = Direction.UP

        loop = 0
        while True:
            loop = loop + 1
            x = guard.pos[0]
            y = guard.pos[1]

            # lol
            if loop > 99999:
                obstruction_count = obstruction_count + 1
                break

            if guard.direction == Direction.UP:
                if y - 1 < 0:
                    break
            elif guard.direction == Direction.RIGHT:
                if x + 1 > 129:
                    break
            elif guard.direction == Direction.DOWN:
                if y + 1 > 129:
                    break
            elif guard.direction == Direction.LEFT:
                if x - 1 < 0:
                    break

            if guard.direction == Direction.UP:
                if all_coordinates[(x, y - 1)] == "#":
                    guard.turn_right()
                else:
                    guard.pos = (x, y - 1)
                visited_positions.add((guard.pos[0], guard.pos[1], guard.direction))
            elif guard.direction == Direction.RIGHT:
                if all_coordinates[(x + 1, y)] == "#":
                    guard.turn_right()
                else:
                    guard.pos = (x + 1, y)
                visited_positions.add((guard.pos[0], guard.pos[1], guard.direction))
            elif guard.direction == Direction.DOWN:
                if all_coordinates[(x, y + 1)] == "#":
                    guard.turn_right()
                else:
                    guard.pos = (x, y + 1)
                visited_positions.add((guard.pos[0], guard.pos[1], guard.direction))
            elif guard.direction == Direction.LEFT:
                if all_coordinates[(x - 1, y)] == "#":
                    guard.turn_right()
                else:
                    guard.pos = (x - 1, y)
                visited_positions.add((guard.pos[0], guard.pos[1], guard.direction))
        all_coordinates[coordPair] = '.'

    print(obstruction_count)


def run():
    part_one()
    part_two()


if __name__ == "__main__":
    run()
