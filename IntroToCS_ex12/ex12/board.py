import numpy as np

COLUMN_COUNT = 7
ROW_COUNT = 6


class Board:
    """
    this object created to deal with the board of the game itself.
    """
    def __init__(self):
        """
        this function define the Board object.
        self._board: the board itself.
        """
        self._board = Board._create_new_board()

    def __str__(self):
        """
        :return: the printable version of the object.
        """
        return '\n'.join(' '.join(map(str, row)) for row in self._board)

    def get_board_string(self):
        """
        :return: the printable version of the object.
        """
        return self.__str__()

    def get_board_width(self):
        """
        :return: the board width.
        """
        return ROW_COUNT

    def get_board(self):
        """
        :return: the self._board of this specific board.
        """
        return self._board

    def get_free_spot(self, col):
        """
        :param col: the wanted column.
        :return: "False" if full, the index of the free highest cell.
        """
        empty_indexes = np.where(self._board[:, col] == 0)
        if len(empty_indexes) < 1:
            return False

        empty_indexes = empty_indexes[0]
        empty_indexes = empty_indexes.tolist()

        if len(empty_indexes) == 0:
            return -1
        else:
            return empty_indexes[0]

    def add_disc(self, col, player_num):
        """
        adds disc to the board for specific column, if possible.
        :param col: the wanted column
        :param player_num: the number of the player who tries to put in a disc.
        :return: True if success, False else.
        """
        empty_spot = self.get_free_spot(col)
        if empty_spot == -1:
            return False
        else:
            self._board[empty_spot][col] = player_num

    def validate_col(self, col):
        """
        checks if the index of the column is valid.
        :param col: an index of a column.
        :return: True if valid, False else.
        """
        if col >= COLUMN_COUNT or col < 0:
            return False

        if self._board.item((ROW_COUNT - 1, col)) != 0:
            return False

        return True

    def board_full(self):
        """
        checks of the board is full using NumPy.
        :return: Searches for zeroes,
        if founded - return False, else - Return True.
        """
        return not np.isin(self._board.all(), [0])

    def winner_exist(self):
        """
        checks if someone won, looking for four discs if a row, column or
        diagonal.
        :return: True if won, False else.
        """
        item = Board._matrix_win(self._board)
        if item is not None:
            return item
        else:
            item = Board._matrix_win(np.matrix.transpose(self._board))
            if item is not None:
                return item
            else:
                item = Board._matrix_win(
                        Board._get_diagonals_of_matrix(self._board))
                if item is not None:
                    return item
        return None

    @staticmethod
    def _get_diagonals_of_matrix(arr):
        """
        :param arr: index
        :return: diagonals as list.
        """
        diags = [arr[::-1, :].diagonal(i) for i in
                 range(-arr.shape[0] + 1, arr.shape[1])]

        diags.extend(
            arr.diagonal(i) for i in range(arr.shape[1] - 1, -arr.shape[0], -1))

        return [n.tolist()for n in diags]

    @staticmethod
    def _line_win(lst):
        """
        checks if there is 4 "full" cells.
        :param lst: list of arguments from the board of the game.
        :return: True of False (if nobody won in this row.
        """
        current_item = -1
        current_item_count = 0
        item_num = 0
        for item in lst:
            if current_item != item:
                item_num = item
                current_item = item
                current_item_count = 0

            if current_item > 0:
                current_item_count += 1

            if current_item_count == 4:
                return item
        return None

    @staticmethod
    def _matrix_win(matrix):
        """
        :param matrix: list of lists.
        :return: True if someone won in the matrix, False else.
        """
        for lst in matrix:
            item = Board._line_win(lst)
            if item is not None:
                return item
        return None

    @staticmethod
    def _create_new_board():
        """
        Get current board by COL_COUNT
        and ROW_COUNT constants
        :return: List of lists of cells
        """
        return np.zeros((ROW_COUNT, COLUMN_COUNT))
