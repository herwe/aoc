def part_one():
    my_map = {
        "forward": [],
        "down": [],
        "up": [],
    }

    with open("input.txt", "r") as my_input:
        for i in my_input:
            my_map[i.split()[0]].append(int(i.split()[1]))

    final_sum = sum(my_map['forward']) * (sum(my_map['down']) - sum(my_map['up']))
    print(f"Day 2, part one answer is: {final_sum}")


# For a better solution, reuse map from part_one, however, I want to treat them as separate solutions.

def part_two():
    my_map = {
        "forward": [],
        "depth": 0,
        "aim": 0,
    }

    with open("input.txt", "r") as my_input:
        for i in my_input:
            if i.split()[0] == 'down':
                my_map['aim'] += int(i.split()[1])
            elif i.split()[0] == 'up':
                my_map['aim'] -= int(i.split()[1])
            elif i.split()[0] == 'forward':
                my_map['depth'] += (my_map['aim'] * int(i.split()[1]))
                my_map['forward'].append(int(i.split()[1]))

    final_sum = sum(my_map['forward']) * my_map['depth']
    print(f"Day 2, part two answer is: {final_sum}")


def run():
    part_one()
    part_two()


if __name__ == "__main__":
    run()
