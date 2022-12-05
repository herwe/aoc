import re

cargo = [['D', 'M', 'S', 'Z', 'R', 'F', 'W', 'N'], ['W', 'P', 'Q', 'G', 'S'], ['W', 'R', 'V', 'Q', 'F', 'N', 'J', 'C'],
         ['F', 'Z', 'P', 'C', 'G', 'D', 'L'], ['T', 'P', 'S'], ['H', 'D', 'F', 'W', 'R', 'L'], ['Z', 'N', 'D', 'C'],
         ['W', 'N', 'R', 'F', 'V', 'S', 'J', 'Q'], ['R', 'M', 'S', 'G', 'Z', 'W', 'V']]

cargo2 = [['D', 'M', 'S', 'Z', 'R', 'F', 'W', 'N'], ['W', 'P', 'Q', 'G', 'S'], ['W', 'R', 'V', 'Q', 'F', 'N', 'J', 'C'],
         ['F', 'Z', 'P', 'C', 'G', 'D', 'L'], ['T', 'P', 'S'], ['H', 'D', 'F', 'W', 'R', 'L'], ['Z', 'N', 'D', 'C'],
         ['W', 'N', 'R', 'F', 'V', 'S', 'J', 'Q'], ['R', 'M', 'S', 'G', 'Z', 'W', 'V']]
def swap_and_delete(commands):
    #to_append = cargo[(commands[2]-1)]
    #to_remove = cargo[(commands[1]-1)]
    move = commands[0]

    for i in range(move):
        if cargo[(commands[1]-1)]:
            cargo[(commands[2]-1)].append(cargo[(commands[1]-1)].pop())
    #print(cargo[(commands[2]-1)])
    #print(cargo[(commands[1]-1)])
    #print(move)
    #print(cargo)
    print()


def part_one():
    with open("input.txt", "r") as f:
        for line in f.read().splitlines():
            commands = [int(s) for s in line.split() if s.isdigit()]
            swap_and_delete(commands)
        for container in cargo:
            if container:
                print(container.pop(), end='')

if __name__ == "__main__":
    part_one()
