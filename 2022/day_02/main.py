conditions = {'A': {'Z': 3, 'X': 4, 'Y': 8}, 'B': {'X': 1, 'Y': 5, 'Z': 9}, 'C': {'Y': 2, 'Z': 6, 'X': 7}}
conditions_two = {'A': [3, 4, 8], 'B': [1, 5, 9], 'C': [2, 6, 7]}

def part_one():
    with open("input.txt", "r") as f:
        sum = 0
        for line in f.read().splitlines():
            values = line.split()
            opponent_shape = values[0]
            player_shape = values[1]
            points = conditions[opponent_shape][player_shape]
            sum += points
        print(f"Day 2, answer 1: {sum}")

def part_two():
    with open("input.txt", "r") as f:
        sum = 0
        for line in f.read().splitlines():
            values = line.split()
            opponent_shape = values[0]
            round_ending_condition = values[1]
            if round_ending_condition == 'X':
                sum += conditions_two[opponent_shape][0]
            elif round_ending_condition == 'Y':
                sum += conditions_two[opponent_shape][1]
            elif round_ending_condition == 'Z':
                sum += conditions_two[opponent_shape][2]
        print(f"Day 2, answer 2: {sum}")

if __name__ == "__main__":
    part_one()
    part_two()
