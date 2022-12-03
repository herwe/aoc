item_type = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

item_prioritize = {}
for index, letter in enumerate(item_type):
    item_prioritize[letter] = index + 1


def part_one():
    with open("input.txt", "r") as f:
        sum = 0
        for line in f.read().splitlines():
            first_part, second_part = line[:len(line) // 2], line[len(line) // 2:]
            sum += item_prioritize[set(first_part).intersection(set(second_part)).pop()]
        print(f"Day 3, part one answer: {sum}")


def part_two():
    with open("input.txt", "r") as f:
        sum = 0
        group = []
        for line in f.read().splitlines():
            group.append(line)
            if len(group) == 3:
                first, second, third = group[0], group[1], group[2]
                intersect = set(first) & set(second) & set(third)
                sum += item_prioritize[intersect.pop()]
                group.clear()
        print(f"Day 3, part two answer: {sum}")


if __name__ == "__main__":
    part_one()
    part_two()
