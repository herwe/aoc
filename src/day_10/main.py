import re


def run():
    part_one()


def part_one():
    with open("input.txt", "r") as f:
        input_arr = f.read().splitlines()

    count_values = {')': 3,
                    ']': 57,
                    '}': 1197,
                    '>': 25137}
    count = []
    clean_array = []
    for i in input_arr:
        for _ in range(100):
            i = re.sub("\(\)", "", i)
            i = re.sub("\[\]", "", i)
            i = re.sub("\{\}", "", i)
            i = re.sub("\<\>", "", i)
        clean_array.append(i)

    for j_index, j in enumerate(clean_array):
        for k_index, k in enumerate(j):
            if k_index == len(j) - 1:
                break
            if has_valid_bracket_format(k, j[k_index + 1]):
                count.append(count_values[j[k_index + 1]])
                break

    print(f"Day 10, part 1 answer is: {sum(count)}")


def has_valid_bracket_format(current, compare):
    if current == "(" and has_valid_closing_bracket(compare):
        return True
    elif current == '[' and has_valid_closing_bracket(compare):
        return True
    elif current == '{' and has_valid_closing_bracket(compare):
        return True
    elif current == '<' and has_valid_closing_bracket(compare):
        return True

    return False


def has_valid_closing_bracket(current_check):
    if current_check == ')' or current_check == ']' or current_check == '}' or current_check == '>':
        return True

    return False


if __name__ == "__main__":
    run()
