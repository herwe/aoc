def parts(part, marker):
    with open("input.txt", "r") as f:
        line = f.read()
        for index, i in enumerate(line):
            if len(set(line[(index - marker):index])) == marker:
                print(f"Day 6, part {part} is : {index}")
                break


if __name__ == "__main__":
    parts(1, 4)
    parts(2, 14)
