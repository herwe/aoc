import copy


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
    counter_ones = 0
    counter_zeros = 0
    current = -1
    with open("test.txt", "r") as my_input:
        my_input_list = [i for i in my_input]

    my_copy = copy.deepcopy(my_input_list)
    count_list = []

    join_characters(count_list, my_input_list)

    my_input_list = rating_generator(count_list, counter_ones, counter_zeros, current, my_input_list)
    my_copy = rating_generator_2(count_list, counter_ones, counter_zeros, current, my_copy)

    final_sum = int(int(''.join(my_input_list), 2)) * (int(''.join(my_copy), 2))
    print(f"Day 3, part two answer is: {final_sum}")


def rating_generator(count_list, counter_ones, counter_zeros, current, my_input_list):
    for index, i in enumerate(count_list):
        for j in i:
            if j == '1':
                counter_ones += 1
            elif j == '0':
                counter_zeros += 1

        if len(my_input_list) == 2:
            current = '1'
        else:
            if counter_ones > counter_zeros:
                current = '1'
            elif counter_ones < counter_zeros:
                current = '0'

        counter_zeros = 0
        counter_ones = 0

        temp_list = []

        for k_index, k in enumerate(my_input_list):
            if k[index] != current:
                temp_list.append(k)
        my_input_list = [i for i in my_input_list if i not in temp_list]

        if len(my_input_list) == 1:
            return my_input_list

        count_list = join_characters(count_list, my_input_list)


def rating_generator_2(count_list, counter_ones, counter_zeros, current, my_input_list):
    for index, i in enumerate(count_list):
        for j in i:
            if j == '1':
                counter_ones += 1
            elif j == '0':
                counter_zeros += 1

        if len(my_input_list) == 2:
            current = '0'
        else:
            if counter_ones > counter_zeros:
                current = '0'
            elif counter_ones < counter_zeros:
                current = '1'

        counter_zeros = 0
        counter_ones = 0

        temp_list = []

        for k_index, k in enumerate(my_input_list):
            if k[index] != current:
                temp_list.append(k)
        my_input_list = [i for i in my_input_list if i not in temp_list]

        if len(my_input_list) == 1:
            return my_input_list

        count_list = join_characters(count_list, my_input_list)


def join_characters(count_list, my_input_list):
    for index, _ in enumerate(range(5)):
        temp = list(zip(*my_input_list))[index]
        ''.join(temp)
        count_list.append(''.join(temp))

    return count_list


def run():
    first_part()
    second_part()


if __name__ == "__main__":
    run()
