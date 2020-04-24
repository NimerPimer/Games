"""
This is an improvement to the knight's tour algorithm.
It uses Warnsdorff's rule.

Every iteration we move to the place that has the minimum amount of possible moves (the next moves).
If 2 places (can be more then 2) have the same amount of moves after them, we'll chose a random one (from those 2).

It works in a reasonable amount of time for 31x31 boards (in my machine).
"""

import random

BOARD_SIZE = 31

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
        rnd_move = correct_move(i, j, moves, solution)
        i += Knight_Moves[rnd_move][0]
        j += Knight_Moves[rnd_move][1]
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


def correct_move(i, j, moves, solution):

    next_step_moves = []
    for move in moves:
        next_step_moves.append(possible_moves(i + Knight_Moves[move][0],
                                              j + Knight_Moves[move][1], solution))

    return moves[random_shortest_list(next_step_moves)]


def random_shortest_list(input_list_of_lists):
    lengths = []
    for i in range(len(input_list_of_lists)):
        lengths.append(len(input_list_of_lists[i]))

    min_value = min(lengths)
    possible_positions = []
    for i in range(len(lengths)):
        if lengths[i] == min_value:
            possible_positions.append(i)

    return random.choice(possible_positions)


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

