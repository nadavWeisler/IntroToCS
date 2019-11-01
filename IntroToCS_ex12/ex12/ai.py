from .player import Player
import random
from copy import copy, deepcopy
import random


class AI():
    def __init__(self, game, player, level=2):
        self.game = game
        self.player = player
        self.level = level

    def get_player_name(self):
        return self.player.get_name()

    def get_last_found_move(self):
        pass

    def find_legal_move(self, timeout=None):
        """
        Find legal move of AI
        :param timeout:
        :return: move
        """
        board = self.game.get_board()
        potential_moves = \
            self._get_all_potential_moves(board,
                                          board.get_board_width(),
                                          self.level)
        best_move_fitness = -1
        for i in range(board.get_board_width()):
            if potential_moves[i] > best_move_fitness and \
                    self.game.validate_col(i):
                best_move_fitness = potential_moves[i]
        best_moves = []
        for i in range(len(potential_moves)):
            if potential_moves[i] == best_move_fitness and \
                    self.game.validate_col(i):
                best_moves.append(i)
        if best_moves == []:
            return random.choice(potential_moves)
        return random.choice(best_moves)

    def _get_all_potential_moves(self, board, bored_width, level):
        """
        Get list of all potential moves
        :param board: current board
        :return: list of moves
        """
        print(level)
        if level <= 0 or self.game.get_winner() is not None:
            return [0] * bored_width

        potential_moves = [0] * bored_width
        for first_move in range(bored_width):
            duplicate_board = deepcopy(board)
            if not self.game.validate_col(first_move):
                continue

            duplicate_board.add_disc(first_move,
                                     self.game.get_current_player())

            if duplicate_board.winner_exist():
                potential_moves[first_move] = 1
                break
            else:
                if duplicate_board.board_full():
                    potential_moves[first_move] = 0
                else:
                    for manual_move in range(bored_width):
                        duplicate_board2 = deepcopy(duplicate_board)
                        if not self.game.validate_col(manual_move):
                            continue
                        duplicate_board2.add_disc(manual_move,
                                                  self.game.get_rival_player())
                        if duplicate_board2.winner_exist():
                            potential_moves[first_move] = -1
                            break
                        else:
                            results = self._get_all_potential_moves(
                                duplicate_board2, bored_width, level - 1)
                            potential_moves[first_move] += \
                                (sum(results) / bored_width) / \
                                bored_width
        return potential_moves
