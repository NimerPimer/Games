"""
This is a brute force algorithm for finding Knight's tours from a random starting point.
It works in a reasonable amount of time for 5x5 boards.

"""

import random

BOARD_SIZE = 5

Knight_Moves = {0: [2, 1],
                1: [2, -1],
                2: [-2, 1],
                3: [-2, -1],
                4: [1, 2],
                5: [-1, 2],
                6: [1, -2],
                7: [-1, -2]}


def knight(solution):

    if len(solution) == BOARD_SIZE*BOARD_SIZE:
        print(solution)

    # Knight's current location
    i = solution[len(solution) - 1][0]
    j = solution[len(solution) - 1][1]

    moves = possible_moves(i, j, solution)

    while len(moves) > 0:
        # Knight moves
        rnd_move = random.choice(moves)
        i += Knight_Moves[rnd_move][0]
        j += Knight_Moves[rnd_move][1]
        if (i, j) not in solution and in_board(i, j):
            solution.append((i, j))
            knight(solution)
            solution.pop()
            i -= Knight_Moves[rnd_move][0]
            j -= Knight_Moves[rnd_move][1]
            moves.remove(rnd_move)
    return


def possible_moves(i, j, solution):
    possible_moves_list = []
    for move in range(8):
        next_i = i + Knight_Moves[move][0]
        next_j = j + Knight_Moves[move][1]
        if (next_i, next_j) not in solution and in_board(next_i, next_j):
            possible_moves_list.append(move)
    return possible_moves_list


def in_board(i, j):
    if i in range(BOARD_SIZE) and j in range(BOARD_SIZE):
        return True
    else:
        return False


def main():

    start_i = random.randrange(0, BOARD_SIZE)
    start_j = random.randrange(0, BOARD_SIZE)
    solution = [(start_i, start_j)]
    knight(solution)


if __name__ == "__main__":
    main()

