from .board import Board
import random
from .player import Player


COL_COUNT = 7
ROW_COUNT = 6


class Game:
    def __init__(self, player1=None, player2=None, level=2):
        """
        the game object - anything that printed on the screen happends here.
        self._board = a Board object.
        self._player1 = the first player (Player object)
        self._player2 = the second player (Player object)
        self._current_player = the player which plays now. The first player
        is chosen randomly.
        self.level = the level of the level, if ai is/are playing.
        """
        self._board = Board()
        self._player1 = player1
        if self._player1 is None:
            self._player1 = Player()
        self._player2 = player2
        if self._player2 is None:
            self._player2 = Player(self._player1.get_name())
        self._current_player = random.choice([self._player1, self._player2])
        self.ai1 = None
        self.ai2 = None

    def __str__(self):
        """
        :return:the printable version of the Game object.
        """
        return self._board.get_board_string()

    def append_ai(self, ai1, ai2):
        if self._player1.player_is_ai():
            self.ai1 = ai1
        if self._player2.player_is_ai():
            self.ai2 = ai2
            
    def make_move(self, column):
        """
        makes a single move of the game.
        :param column: the wanted column to put in a disc.
        :param player: Player object (that plays the game)
        :return:
        """
        if self.validate_col(column):
            self._board.add_disc(column,
                                 self._current_player.get_player_number())
        else:
            raise Exception("Illegal move")

    def get_players(self):
        """
        :return: the player that plays in the current game.
        """
        return self._player1, self._player2

    def get_current_player(self):
        if self._current_player.get_name() == self._player1.get_name():
            return 1
        else:
            return 2

    def get_current_player_object(self):
        """
        :return: the player that plays right now.
        """
        return self._current_player

    def get_rival_player(self):
        """
        :return: the rival player of the current player.
        """
        if self._player1.get_name() == self._current_player.get_name():
            return self._player2.get_player_number()
        else:
            return self._player1.get_player_number()

    def get_board(self):
        return self._board

    def _validate_row(self, row):
        if 0 <= row < ROW_COUNT:
            return True
        return False

    def _check_location(self, row, col):
        if not (self.validate_col(col) and self._validate_row(row)):
            return False
        return True

    def get_player_at(self, row, col):
        """
        :param row: the row index.
        :param col: the column index.
        :return: the contest of the cell in the given row and column.
        """
        if not self._check_location(row, col):
            raise Exception("Illegal location.")
        current = self._board.get_board().item((row, col))
        if current:
            return current
        else:
            return None

    def get_winner(self):
        """
        :return: ends the game - if full with no winner, returns "draw".
        Else - returns "winner".
        """
        winner = self._board.winner_exist()
        if winner is not None:
            return winner

        if self._board.board_full():
            return 0

        return None

    def _end_turn(self):
        """
        ends a turn.
        :return: the next player.
        """
        if self.get_winner():
            return self._current_player
        else:
            if self._current_player == self._player2:
                self._current_player = self._player1
            else:
                self._current_player = self._player2

    def one_turn_ai(self):
        """
        :return: making a move of ai.
        """
        if self.ai1 is not None and\
                self._current_player.get_name() == self.ai1.get_player_name():
            choice = self.ai1.find_legal_move()
        else:
            choice = self.ai2.find_legal_move()

        self.one_turn(choice)

    def one_turn(self, col):
        """
        :param col: the wanted column
        :return: the function that ends turn.
        """
        self.make_move(col)
        return self._end_turn()

    def current_player_is_ai(self):
        """
        :return: if the current player is ai or not. (boolian)
        """
        return self._current_player.player_is_ai()

    def get_cell_value(self, row, col):
        """
        :param row: the specific row
        :param col: the specific column
        :return: the content of the cell in the given index.
        """
        return self._board.get_board()[row][col]

    def validate_col(self, col):
        """
        checks if the index of the column is valid.
        :param col: an index of a column.
        :return: True if valid, False else.
        """
        if self._board.validate_col(col):
            return True
        else:
            raise Exception("Illegal Move")
