cargo = [['D', 'M', 'S', 'Z', 'R', 'F', 'W', 'N'], ['W', 'P', 'Q', 'G', 'S'], ['W', 'R', 'V', 'Q', 'F', 'N', 'J', 'C'],
         ['F', 'Z', 'P', 'C', 'G', 'D', 'L'], ['T', 'P', 'S'], ['H', 'D', 'F', 'W', 'R', 'L'], ['Z', 'N', 'D', 'C'],
         ['W', 'N', 'R', 'F', 'V', 'S', 'J', 'Q'], ['R', 'M', 'S', 'G', 'Z', 'W', 'V']]

cargo2 = [['D', 'M', 'S', 'Z', 'R', 'F', 'W', 'N'], ['W', 'P', 'Q', 'G', 'S'], ['W', 'R', 'V', 'Q', 'F', 'N', 'J', 'C'],
          ['F', 'Z', 'P', 'C', 'G', 'D', 'L'], ['T', 'P', 'S'], ['H', 'D', 'F', 'W', 'R', 'L'], ['Z', 'N', 'D', 'C'],
          ['W', 'N', 'R', 'F', 'V', 'S', 'J', 'Q'], ['R', 'M', 'S', 'G', 'Z', 'W', 'V']]

def swap_and_delete(commands):
    move = commands[0]
    temp = []
    for i in range(move):
        if cargo[(commands[1] - 1)]:
            removed = cargo[(commands[1] - 1)].pop()
            cargo[(commands[2] - 1)].append(removed)
        if cargo2[(commands[1] - 1)]:
            removed2 = cargo2[(commands[1] - 1)].pop()
            temp.append(removed2)
    for item in reversed(temp):
        cargo2[(commands[2] - 1)].append(item)


def part_one():
    answer1 = ''
    answer2 = ''
    with open("input.txt", "r") as f:
        for line in f.read().splitlines():
            commands = [int(s) for s in line.split() if s.isdigit()]
            swap_and_delete(commands)
        for container in cargo:
            if container:
                answer1 = answer1 + container.pop()
        for container in cargo2:
            if container:
                answer2 = answer2 + container.pop()
        print(f"Day 5, part 1: {answer1}\nDay 5, part 2: {answer2}")

if __name__ == "__main__":
    part_one()
