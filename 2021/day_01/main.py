def part_one():
    my_input = open("input.txt")
    count = loop_through_input(my_input)
    my_input.close()
    print(f"Day 1, part 1 answer is: {count}")


def loop_through_input(my_input):
    number = int(my_input.readline())
    count = 0
    for line in my_input:
        current = int(line)
        if number < current:
            count += 1
        number = current
    return count


def part_two():
    my_input = open("input.txt")
    my_input_list = [int(line) for line in my_input]
    sum_list = []
    try:
        for index, i in enumerate(my_input_list):
            current_sum = my_input_list[index] + my_input_list[index + 1] + my_input_list[index + 2]
            sum_list.append(current_sum)
    except IndexError:
        loop_through_numbers(sum_list)


def loop_through_numbers(sum_list):
    count = 0
    number = sum_list[0]
    for num in sum_list[1:]:
        current = num
        if number < current:
            count += 1
        number = current

    print(f"Day 1, part 2 answer: {count}")


def run():
    part_one()
    part_two()


if __name__ == "__main__":
    run()
