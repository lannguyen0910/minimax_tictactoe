import math
from helper import print_board, empty_cells, check_current_state, player_move, evaluate_play

players = ['X', 'O']


def minimax_alpha_beta_pruning(state, player_turn, alpha=-math.inf, beta=math.inf):
    winner, current_state = check_current_state(state)
    if current_state == 'Draw' or current_state == 'Done':
        return {'score': evaluate_play(current_state, winner), "move": "-1 -1"}

    best = {}
    if player_turn == 'X':
        best['score'] = -math.inf
        best['move'] = ""
    else:
        best['score'] = math.inf
        best['move'] = ""

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player_turn
        if player_turn == 'O':
            result = minimax_alpha_beta_pruning(state, "X", alpha, beta)
        else:
            result = minimax_alpha_beta_pruning(state, "O", alpha, beta)

        state[x][y] = " "  # make cell empty because of recursion
        result['move'] = "{} {}".format(x, y)

        # X is AI turn, we want to maximize the AI's score
        if player_turn == 'X':
            if result['score'] > best['score']:
                best = result
                alpha = max(best['score'], alpha)

        # O is Human turn, we want to minimize the human's score
        else:
            if result['score'] < best['score']:
                best = result
                beta = min(best['score'], beta)

        if alpha >= beta:
            break

    return best


if __name__ == '__main__':
    playing = True

    while(playing):
        print('TIC TAC TOE! Can you beat our AI?')
        print("========================================")
        game_state = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        state = "Playing"
        print_board(game_state)

        while True:
            player = input(
                "Please select player to go first (O is you, X is computer): ").upper()
            if player in players:
                if player == 'X':
                    player_id = 0
                else:
                    player_id = 1
                break
            else:
                print('Please enter a valid selection!!!')

        while state == 'Playing':
            if player == "O":
                player_input = input(
                    "Your turn. Please choose a position by entering 2 numbers seperated by a space to place your mark (e.g. row column - 2 1): ")
                player_move(game_state, player_input, player)
                print('You placed the "O" on {}'.format(
                    player_input))

            else:
                print('AI turn.')
                position = minimax_alpha_beta_pruning(game_state, player)
                player_move(game_state, position['move'], player)
                print('The computer placed the "X" on {}'.format(
                    position['move']))

            print_board(game_state)
            print('- - - - - - - - - - - - - - - - - - - -')

            winner, state = check_current_state(game_state)

            if winner is not None:
                if winner == 'X':
                    print("AI won!")
                else:
                    print("You won!")

            else:
                # Switch turn
                player_id = (player_id + 1) % 2
                player = players[player_id]

            if state == 'Draw':
                print('Its a tie!')

        print("-----------------------------------------")
        restart = input('Do you wanna play again? (Y/N): ').upper()
        if restart == "N":
            print('Thanks for playing')
            playing = False
