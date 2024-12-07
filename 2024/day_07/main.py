from itertools import product


def run():
    part_one()
    part_two()


def part_one():
    calibrations = {}
    with open("input.txt", "r") as f:
        for line in f.readlines():
            line = line.replace(":", "")
            line = line.split()
            calibrations[int(line[0])] = [int(x) for x in line[1:]]

    test_value_sum = 0
    for test_value in calibrations:
        equation = calibrations[test_value]

        operators = ['+', '*']
        operator_combinations = list(product(operators, repeat=len(equation) - 1))

        for ops in operator_combinations:
            result = equation[0]
            for num, op in zip(equation[1:], ops):
                if op == '+':
                    result += num
                elif op == '*':
                    result *= num
            if result == test_value:
                test_value_sum = test_value_sum + test_value
                break

    print(test_value_sum)


def part_two():
    calibrations = {}
    with open("input.txt", "r") as f:
        for line in f.readlines():
            line = line.replace(":", "")
            line = line.split()
            calibrations[int(line[0])] = [int(x) for x in line[1:]]

    test_value_sum = 0
    for test_value in calibrations:
        equation = calibrations[test_value]

        operators = ['+', '*', '||']
        operator_combinations = list(product(operators, repeat=len(equation) - 1))

        for ops in operator_combinations:
            result = equation[0]
            for num, op in zip(equation[1:], ops):
                if op == '+':
                    result += num
                elif op == '*':
                    result *= num
                elif op == '||': # string concatenate operation, then convert back to a number
                    tmp = list(str(result))
                    tmp.append(str(num))
                    result = int(''.join(tmp))
            if result == test_value:
                test_value_sum += test_value
                break

    print(test_value_sum)


if __name__ == "__main__":
    run()
