def run():
    part_one()
    part_two()


def part_one():
    left_list = []
    right_list = []
    with open("input.txt", "r") as f:
        for line in f:
            line = line.replace('\n', '')
            line = line.split()
            left_list.append(int(line[0]))
            right_list.append(int(line[1]))
    left_list.sort()
    right_list.sort()
    sum = 0
    for index, num in enumerate(left_list):
        sum = sum + max(left_list[index], right_list[index]) - min(left_list[index], right_list[index])
    print(sum)


def part_two():
    left_list = []
    right_list = []
    with open("input.txt", "r") as f:
        for line in f:
            line = line.replace('\n', '')
            line = line.split()
            left_list.append(int(line[0]))
            right_list.append(int(line[1]))

        occurrences = {}
        for num in right_list:
            occurrences[num] = right_list.count(num)

        sum = 0
        for num in left_list:
            if occurrences.get(num) is not None:
                sum = sum + (num * occurrences[num])

        print(sum)


if __name__ == "__main__":
    run()
