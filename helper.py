""" This helper.py contains some functions to help the Minimax Algorithm and game console. """


def print_board(state):
    print("  -------------------")
    print("  |  {}  |  {}  |  {}  |".format(
        state[0][0], state[0][1], state[0][2]))
    print("  ------+-----+------")
    print("  |  {}  |  {}  |  {}  |".format(
        state[1][0], state[1][1], state[1][2]))
    print("  ------+-----+------")
    print("  |  {}  |  {}  |  {}  |".format(
        state[2][0], state[2][1], state[2][2]))
    print("  -------------------")


def empty_cells(state):
    """
    Return list of empty cells
    """
    cells = []
    for id_r, row in enumerate(state):
        for id_c, cell in enumerate(row):
            if cell == " ":
                cells.append([id_r, id_c])

    return cells


def check_current_state(state):
    # 8 possible winning strategies
    win_state = [[state[1][0], state[1][1], state[1][2]],
                 [state[2][0], state[2][1], state[2][2]],
                 [state[0][0], state[0][1], state[0][2]],
                 [state[0][0], state[1][0], state[2][0]],
                 [state[0][0], state[1][1], state[2][2]],
                 [state[0][2], state[1][1], state[2][0]],
                 [state[0][1], state[1][1], state[2][1]],
                 [state[0][2], state[1][2], state[2][2]]]

    if ['X', 'X', 'X'] in win_state:
        return "X", "Done"
    elif ['O', 'O', 'O'] in win_state:
        return "O", "Done"
    elif len(empty_cells(state)) == 0:
        return None, "Draw"
    else:
        return None, "Playing"


def player_move(state, board_place, player_turn):
    """
    Player play their turn on the board
    """
    while True:
        try:
            row, col = board_place.split(" ")
            if int(row) > 2 or int(col) > 2:
                raise ValueError
            break
        except ValueError:
            board_place = input(
                "Please enter value in this format (e.g: 1 2) and in range (0 -> 2): ")

    if state[int(row)][int(col)] == " ":
        state[int(row)][int(col)] = player_turn
    else:
        board_place = input(
            'The position has already been placed! Choose another strategy: ')
        player_move(state, board_place, player_turn)


def evaluate_play(state, winner):
    """
    Return 1 if AI wins - -1 if Human wins - 0 if it's a tie
    """
    if state == "Done" and winner == 'X':
        return 1
    elif state == 'Done' and winner == 'O':
        return -1
    elif state == 'Draw':
        return 0
