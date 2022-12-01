


def part_one():
    with open("input.txt", "r") as f:
        current_sum = 0
        biggest_sum = 0
        for line in f.read().splitlines():
            if line == '':
                biggest_sum = current_sum if current_sum > biggest_sum else biggest_sum
                current_sum = 0
            else:
                current_sum += int(line)
        print(f"Day 1, solution 1 {biggest_sum}")

def part_two():
    with open("input.txt", "r") as f:
        calories = []
        current_sum = 0
        for line in f.read().splitlines():
            if line == '':
                calories.append(current_sum)
                current_sum = 0
            else:
                current_sum += int(line)
        elves_sorted = sorted(calories, reverse=True)
        print(f"Day 1, solution 2{elves_sorted[0] + elves_sorted[1] + elves_sorted[2]}")


if __name__ == "__main__":
    part_one()
    part_two()
