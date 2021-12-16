

def run():
    print("This will take a few seconds.....")
    with open("input.txt") as file:
        input_list = [int(x) for x in file.read().strip().split(",")]

    part_one = min([sum([max([x, i]) - min([x, i]) for x in input_list]) for i in range(min(input_list), max(input_list))])
    part_two = min([sum([sum(range(1 + max([x, i]) - min([x, i]))) for x in input_list]) for i in range(min(input_list), max(input_list))])

    print(f"Day 7, part one answer is: {part_one}")
    print(f"Day 7, part two answer is: {part_two}")


if __name__ == "__main__":
    run()
