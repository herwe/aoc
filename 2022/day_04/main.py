

def main():
    with open("input.txt", "r") as f:
        first_answer = 0
        second_answer = 0
        for line in f.read().splitlines():
            divider = line.split(',')
            first, second = divider[0].split('-'), divider[1].split('-')
            first_range = []
            second_range = []
            for count in range(int(first[0]), int(first[1]) + 1):
                first_range.append(count)
            for count in range(int(second[0]), int(second[1]) + 1):
                second_range.append(count)
            if set(first_range).issubset(set(second_range)) or set(second_range).issubset(set(first_range)):
                first_answer += 1
            if set(first_range).intersection(set(second_range)) or set(second_range).intersection(set(first_range)):
                second_answer += 1
        print(f"Day 4, answer 1 is {first_answer}")
        print(f"Day 4, answer 2 is {second_answer}")


if __name__ == "__main__":
    main()
