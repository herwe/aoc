def part_one():
    my_map = {
        "forward": [],
        "down": [],
        "up": [],
    }

    my_input = open("input.txt")
    for i in my_input:
        my_map[i.split()[0]].append(int(i.split()[1]))

    my_input.close()
    final_sum = sum(my_map['forward']) * (sum(my_map['down']) - sum(my_map['up']))
    print(f"Day 2, part one answer is: {final_sum}")


def part_two():
    my_map = {
        "forward": [],
        "depth": 0,
        "aim": 0,
    }

    my_input = open("input.txt")

    for i in my_input:
        if i.split()[0] == 'down':
            my_map['aim'] += int(i.split()[1])
        elif i.split()[0] == 'up':
            my_map['aim'] -= int(i.split()[1])
        elif i.split()[0] == 'forward':
            if my_map['aim'] == 0:
                my_map['depth'] += 0
            else:
                my_map['depth'] += (my_map['aim'] * int(i.split()[1]))

            my_map['forward'].append(int(i.split()[1]))

    final_sum = sum(my_map['forward']) * my_map['depth']
    print(f"Day 2, part two answer is: {final_sum}")


def run():
    part_one()
    part_two()


if __name__ == "__main__":
    run()
