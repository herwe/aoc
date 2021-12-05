bingo_numbers = []
non_marked_bingo_numbers = []
correct_marked = ('X', 'X', 'X', 'X', 'X')
winning_bingo_number = 0


def part_one():
    new_arr = []

    with open("test_input.txt", "r") as file:
        drawn_numbers = file.readline().split(',')

    with open("test_input.txt", "r") as file:
        lines = file.read()

    lines = [line.replace(' ', 'BREAK') or line.replace('\n', 'BREAK') for line in lines]
    lines = [line for x, line in enumerate(lines) if x > 71]
    checker = ''
    for i in lines:
        if i.isdigit():
            checker += i
        else:
            new_arr.append(checker)
            checker = ''

    counter = 0
    temp = []
    for i in new_arr:
        if i.isdigit():
            temp.append(int(i))
            counter += 1
        if counter == 5:
            bingo_numbers.append(temp)
            counter = 0
            temp = []
    non_marked_bingo_numbers = bingo_numbers
    mark_bingo_tiles(drawn_numbers)
    # print(bingo_numbers)


def mark_bingo_tiles(drawn_numbers):
    for number in drawn_numbers:
        current_number = int(number)
        for index, i in enumerate(bingo_numbers):
            for inner_index, j in enumerate(i):
                if current_number == j:
                    number_to_be_marked = bingo_numbers[index][inner_index]
                    bingo_numbers[index][inner_index] = "X"
                    check_if_bingo(number_to_be_marked, index)



def check_if_bingo(number_to_be_marked, index):
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    lst = []

    while True:
        try:
            lst += list(zip(bingo_numbers[a], bingo_numbers[b], bingo_numbers[c], bingo_numbers[d], bingo_numbers[e]))
            a += 5
            b += 5
            c += 5
            d += 5
            e += 5
        except IndexError:
            break

    print(lst)
    board_count = 0
    board_index = 0

    loop_and_mark(board_count, board_index, lst, number_to_be_marked)


    board_count = 0
    board_index = 0
    #loop_and_mark(board_count, board_index, bingo_numbers, number_to_be_marked)


def loop_and_mark(board_count, board_index, lst, number_to_be_marked):
    for index, i in enumerate(lst):
        if board_count == 25:
            board_index += 1
            board_count = 0
        for j in range(5):
            board_count += 1
            if tuple(i) == correct_marked:
                print(f"Denna: {lst}")
                calc_sum_of_winning_board(lst, board_index, number_to_be_marked)


def calc_sum_of_winning_board(board, board_index, number_to_be_marked):
    my_start = board_index*5
    end = my_start+5
    end_sum = 0
    print(board)
    for i in range(my_start, end):
        for j in board[i]:
            print(j)
            if j != 'X':
                end_sum += j

    print(end_sum)
    print(end_sum * number_to_be_marked)
    exit(1)




def run():
    part_one()


if __name__ == "__main__":
    run()
