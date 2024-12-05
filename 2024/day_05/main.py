def part_one_and_two():
    rules = []
    updates = []
    middle = []

    with open("rules.txt", "r") as f:
        for line in f:
            before, after = map(int, line.split('|'))
            rules.append((before, after))

    with open("updates.txt", "r") as f:
        for line in f:
            updates.append(list(map(int, line.split(','))))

    for update in updates:
        if is_valid_update(update, rules):
            middle.append(update[len(update) // 2])

    part_one_result = sum(middle)
    print(part_one_result)
    middle.clear()

    for update in updates:
        if not is_valid_update(update, rules):
            bubble_sort(update, rules)
            middle.append(update[len(update) // 2])

    part_two_result = sum(middle)
    print(part_two_result)


def is_valid_update(update, rules):
    for before, after in rules:
        if before in update and after in update:
            if update.index(before) > update.index(after):
                return False
    return True


# I googled how to do bubble sort because I forgot
def bubble_sort(update, rules):
    rule_set = set(rules)
    n = len(update)

    for i in range(n):
        for j in range(n - 1):
            if (update[j + 1], update[j]) in rule_set:  # Violates order
                update[j], update[j + 1] = update[j + 1], update[j]

    return update


def run():
    part_one_and_two()


if __name__ == "__main__":
    run()
