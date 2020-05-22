import random
from copy import deepcopy

def print_board(board, end=""):
    count_y = 0
    for i in board:
        count_x = 0
        for j in i:
            count_x += 1
            print(j if j != 0 else '`', end=('|' if count_x % 3 == 0 and count_x != 9 else ''))
            # Changing the end character
        print("\n", end='')
        count_y += 1
        if (count_y % 3 == 0 and count_y != 9):
            for j in range(6):
                print("--", end='')
            print()
    print(end=end)


def check_valid(c_board, transposed=False):

    # Check horizontal rows
    for i1 in c_board:
        i2 = list(filter(lambda a: a != 0, i1)) # Filter out all zeros
        if (len(i2) != len(set(i2))): # Compare original to set (duplicates removed)
            return False

    # Reflect board along y = (-x)
    if (not transposed):
        board_transpose = deepcopy([list(i) for i in zip(*c_board)])
        return check_valid(board_transpose, True)

    for y_box in range(3):
        for x_box in range(3):
            box_nums = list(c_board[i + y_box*3][j + x_box*3] for i in range(3) for j in range(3)) # Flatten box to list
            box_nums = list(filter(lambda a: a != 0, box_nums))  # Filter out all zeros
            if (len(box_nums) != len(set(box_nums))):  # Compare original to set (duplicates removed)
                return False

    return True



def populate_board(board, init_num_count):
    # Since populate_board generates it randomly,
    # there is a chance that the game may not be solvable.
    # May implement always solvable in a future version.
    for i in range(init_num_count):
        found = False
        count = 0
        while(not found):
            count += 1
            x = random.randint(0,8)
            y = random.randint(0,8)
            if(board[y][x] == 0):
                while(not found):
                    temp_board = deepcopy(board)
                    temp_board[y][x] = random.randint(1,9)
                    if(check_valid(temp_board)):
                        board = deepcopy(temp_board)
                        found = True
    return board


mainb = [[0,0,0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,0,0,],]

mainb = populate_board(mainb, 25) # Should keep initial number count below 40

print_board(mainb)
