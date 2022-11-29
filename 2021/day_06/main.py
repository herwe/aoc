def run(s, solution_range):
    with open("input.txt", "r") as f:
        initial_state = (f.readline().split()[0])
        fish = [int(i) for i in initial_state if i.isdigit()]

    duplicates = {i: fish.count(i) for i in fish}

    for i in range(9):
        if duplicates.get(i) is None:
            duplicates[i] = 0

    for _ in range(solution_range):
        temp0 = duplicates[0]
        temp = duplicates[8]
        duplicates[8] = temp0
        temp2 = duplicates[7]
        duplicates[7] = temp
        temp3 = duplicates[6]
        duplicates[6] = temp2
        temp4 = duplicates[5]
        duplicates[5] = temp3
        duplicates[6] = temp0 + temp2
        temp5 = duplicates[4]
        duplicates[4] = temp4
        temp6 = duplicates[3]
        duplicates[3] = temp5
        temp7 = duplicates[2]
        duplicates[2] = temp6
        temp8 = duplicates[1]
        duplicates[1] = temp7
        duplicates[0] = temp8

    print(s, sum(duplicates.values()))


if __name__ == "__main__":
    run("Day 6, part one is", 80)
    run("Day 6, part two is", 256)
