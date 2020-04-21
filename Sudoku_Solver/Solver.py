from Board import *
from test_board import *


def solve(board):
    if board.board_is_full():
        board.print_board()
        return
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board.board_data[i][j] == EMPTY_VALUE:
                for k in range(1, BOARD_SIZE+1):
                    if board.check_value_possible(i, j, k):
                        board.board_data[i][j] = k
                        solve(board)
                        board.board_data[i][j] = EMPTY_VALUE
                return


def main():
    print("数独 - Sudoku Solver - 数独")
    board = Board(test_board_1)
    solve(board)
    print("数独 - Sudoku Solver - 数独")


if __name__ == "__main__":
    main()
