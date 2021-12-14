
def run():
    with open("input.txt", "r") as f:
        initial_state = (f.readline().split()[0])
        fish = [int(i) for i in initial_state if i.isdigit()]

    append_counter = 0
    for i in range(80):
        for index, number in enumerate(fish):
            if number == 0:
                fish[index] = 6
                append_counter += 1
            else:
                fish[index] -= 1

        for j in range(append_counter):
            fish.append(8)
        append_counter = 0

    print(f"Day 6, part 1 answer is: {len(fish)}")


if __name__ == "__main__":
    run()
