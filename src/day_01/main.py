def run():
    part_one()
    part_two()


def part_one():
    my_input = open("input.txt")
    number = int(my_input.readline())
    count = 0
    for line in my_input:
        current = int(line)
        if number < current:
            count += 1
        number = current
    my_input.close()
    print(f"Day 1, part 1 answer is: {count}")

def part_two():
        


if __name__ == "__main__":
    run()
