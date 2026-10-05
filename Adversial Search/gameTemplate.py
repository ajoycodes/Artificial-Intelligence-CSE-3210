def best_move(state):
    # find the best move
    return move


def winner(state):
    # determine who can win
    return "First player"


def play(state):
    turn = 1

    while not game_over(state):

        move = best_move(state)

        state = make_move(state, move)

        print("Player", turn, "makes move:", move)

        if game_over(state):
            print("Player", turn, "wins!")
            break

        turn = 3 - turn


state = initial_state()
print(winner(state), "wins with perfect play")
play(state)