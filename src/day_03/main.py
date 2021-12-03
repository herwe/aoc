def first_part():
    gamma_rate_count = []
    epsilon_rate_count = []
    counter_one = 0
    counter_zero = 0

    with open("input.txt", "r") as my_input:
        my_input_list = [i for i in my_input]

    updated_list = []

    for index, _ in enumerate(range(12)):
        temp = list(zip(*my_input_list))[index]
        ''.join(temp)
        updated_list.append(''.join(temp))

    for i in updated_list:
        for j in i:
            if j == '1':
                counter_one += 1
            elif j == '0':
                counter_zero += 1

        if counter_one > counter_zero:
            gamma_rate_count.append('1')
            epsilon_rate_count.append('0')
        elif counter_one < counter_zero:
            gamma_rate_count.append('0')
            epsilon_rate_count.append('1')

        counter_one = 0
        counter_zero = 0

    final_sum = int(int(''.join(gamma_rate_count), 2)) * (int(''.join(epsilon_rate_count), 2))
    print(f"Day 3, part on answer is: {final_sum}")



def second_part():
    pass


def run():
    first_part()
    second_part()


if __name__ == "__main__":
    run()
