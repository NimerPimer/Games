BOARD_SIZE = 9
SQUARE_SIZE = 3
EMPTY_VALUE = 0


class Board(object):
    def __init__(self, board_data):
        self.board_data = board_data

    def print_board(self):
        for i in range(BOARD_SIZE):
            print(self.board_data[i])

    def board_is_full(self):
        for i in range(BOARD_SIZE):
            if EMPTY_VALUE in self.board_data[i]:
                return False
        return True

    def check_row(self, i, try_num):
        if try_num in self.board_data[i]:
            return False
        else:
            return True

    def check_column(self, j, try_num):
        column = []
        for i in range(BOARD_SIZE):
            column.append(self.board_data[i][j])
        if try_num in column:
            return False
        else:
            return True

    def check_square(self, i, j, try_num):
        square_i = SQUARE_SIZE * int(i / SQUARE_SIZE)
        square_j = SQUARE_SIZE * int(j / SQUARE_SIZE)
        square = []
        for i in range(square_i, square_i+SQUARE_SIZE):
            for j in range(square_j, square_j + SQUARE_SIZE):
                square.append(self.board_data[i][j])
        if try_num in square:
            return False
        else:
            return True

    def check_value_possible(self, i, j, try_num):
        if self.check_row(i, try_num) and self.check_column(j, try_num) \
                and self.check_square(i, j, try_num):
            return True
        else:
            return False

