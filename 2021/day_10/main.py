import re

count_values_part_one = {')': 3,
                         ']': 57,
                         '}': 1197,
                         '>': 25137}

count_values_part_two = {')': 1,
                         ']': 2,
                         '}': 3,
                         '>': 4}
count = []
input_arr = []
clean_array = []


def run():
    setup_global_variables()
    part_one()
    part_two()


def setup_global_variables():
    with open("input.txt", "r") as f:
        input_arr = f.read().splitlines()

    for i in input_arr:
        for _ in range(100):
            i = re.sub("\(\)", "", i)
            i = re.sub("\[\]", "", i)
            i = re.sub("\{\}", "", i)
            i = re.sub("\<\>", "", i)
        clean_array.append(i)


def part_two():
    for i in clean_array:
        score = 0
        is_invalid_string = False
        for j in reversed(i):
            if j == '(':
                score = (score * 5) + count_values_part_two[')']
            elif j == '[':
                score = (score * 5) + count_values_part_two[']']
            elif j == '{':
                score = (score * 5) + count_values_part_two['}']
            elif j == '<':
                score = (score * 5) + count_values_part_two['>']
            else:
                is_invalid_string = True
                break

        if not is_invalid_string:
            count.append(score)

    sorted_count = sorted(count)
    print(f"Day 10, part 2 answer is: {sorted_count[int(len(sorted_count) / 2)]}")


def part_one():
    for j_index, j in enumerate(clean_array):
        for k_index, k in enumerate(j):
            if k_index == len(j) - 1:
                break
            if has_valid_bracket_format(k, j[k_index + 1]):
                count.append(count_values_part_one[j[k_index + 1]])
                break

    print(f"Day 10, part 1 answer is: {sum(count)}")
    count.clear()


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
