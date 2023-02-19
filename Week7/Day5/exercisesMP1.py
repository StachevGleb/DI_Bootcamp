board = [
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', '-', '-', '-', '|', ' ', '-', '-', '-', ' ', '|', '-', '-', '-', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', '-', '-', '-', '|', ' ', '-', '-', '-', ' ', '|', '-', '-', '-', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
]

board_win_helper = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

which_player = [0]


def display_board():
    print("TIC TAC TOE")
    for key, val in enumerate(board):
        print(''.join(board[key]))
display_board()

def player_input(board_win_helper, which_player,  board):
    row = int(input("Enter row:  "))
    column = int(input("Enter column: "))
    checker = True
    while checker:
        if 3 < row or row < 1:
            row = int(input("Enter row (1, 2 or 3):  "))
        elif 3 < column or column < 1:
            column = int(input("Enter column (1, 2 or 3): "))
        else:
            checker = False
            which_player[0] = which_player[0] + 1
            board_win_helper_func(which_player, row, column)

def board_win_helper_func(which_player, row, column):
    if which_player[0] % 2 == 0 and board_win_helper[row-1][column-1] == ' ':
        board_win_helper[row-1][column-1] = "X"
        change_index(row, column)
    elif which_player[0] % 2 > 0 or which_player[0] % 2 < 0 and board_win_helper[row-1][column-1] == ' ':
        board_win_helper[row-1][column-1] = "O"
        change_index(row, column)
    elif board_win_helper[row-1][column-1] == 'X' or board_win_helper[row-1][column-1] == 'O':
        print("Chose another position")
        which_player[0] = which_player[0] - 1
def change_index(row, column):
    if row == 2:
         row = 3
    elif row == 3:
        row = 5
    if column == 1:
        column = 2
    elif column == 2:
        column = 8
    elif column == 3:
        column = 14
    which_pl_cheker(which_player, board, row, column)

def is_win_by_row_column():
    for i in range(3):
        if (board_win_helper[i][0] == "X" and board_win_helper[i][1] == "X" and board_win_helper[i][2] == "X") or\
            (board_win_helper[0][i] == "X" and board_win_helper[1][i] == "X" and board_win_helper[2][i] == "X"):
            print("\"X\" winner win")
        elif (board_win_helper[i][0] == "O" and board_win_helper[i][1] == "O" and board_win_helper[i][2] == "O") or\
            (board_win_helper[0][i] == "O" and board_win_helper[1][i] == "O" and board_win_helper[2][i] == "O"):
            print("\"O\" winner win")

def is_win_by_diagonal():
    if (board_win_helper[0][0] == "X" and board_win_helper[1][1] == "X" and board_win_helper[2][2] == "X") or \
    (board_win_helper[0][2] == "X" and board_win_helper[1][1] == "X" and board_win_helper[2][0] == "X"):
        print("\"X\" winner win")
    elif (board_win_helper[0][0] == "O" and board_win_helper[1][1] == "O" and board_win_helper[2][2] == "O") or \
            (board_win_helper[0][2] == "O" and board_win_helper[1][1] == "O" and board_win_helper[2][0] == "O"):
        print("\"O\" winner win")
    else:
        player_input(board_win_helper, which_player, board)

def check_win():
    is_win_by_row_column()
    is_win_by_diagonal()



def which_pl_cheker(which_player, board, row, column):
    if which_player[0] % 2 == 0:
        board[row][column] = "X"
        display_board()
        print("Player O's turn ...")
        check_win()
    elif which_player[0] % 2 > 0 or which_player[0] % 2 < 0:
        board[row][column] = "O"
        display_board()
        print("Player X's turn ...")
        check_win()

player_input(board_win_helper, which_player, board)