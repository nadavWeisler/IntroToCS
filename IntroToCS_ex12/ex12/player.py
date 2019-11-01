import random

class Player:

    def __init__(self, exist_player=None, ai=False, level=2):
        """
        define general object of player - manual or ai.
        self._name = the name of the player.
        self._number = the number of the player.
        self._color = the color of the discs of the player.
        self._level = the level of the ai, if the player is ai.
        self._is_ai = True if ai, False if manual.
        """
        self._name = self._get_random_name(exist_player)
        self._number = self._get_number(exist_player)
        self._color = self._get_color(self._name)
        self._level = level
        self._is_ai = ai

    def get_player_level(self):
        """
        :return: the player level.
        """
        return self._level

    def player_is_ai(self):
        """
        :return: if the player is ai or not (boolean).
        """
        return self._is_ai

    def _get_number(self, exist_player):
        """
        :param exist_player: player, if there is already. None else.
        :return: number of a player.
        """
        if exist_player is None:
            return 1
        else:
            return 2

    def get_player_number(self):
        """
        :return: the number of the player.
        """
        return self._number

    def _get_random_name(self, exist_player):
        """
        names the player with name from "A Tale of Five Balloons".
        :param exist_player: player, if there is already. None else.
        :return: a valid name (non-taken)
        """
        names = ["Ruti", "Ron", "Sigalit", "Uri", "Alon"]
        if exist_player is not None:
            names.remove(exist_player)
        return random.choice(names)

    def get_name(self):
        """
        :return: the name of the player.
        """
        return self._name

    def get_player_color(self):
        """
        :return: the color of the discs of the player.
        """
        return self._color

    def _get_color(self, name):
        """
        :param name: the name of the player.
        :return: the color by the name from "A Tale of Five Balloons".
        """
        my_baloon = {
            "Ruti": "#5494C4",
            "Ron": "#FAE91D",
            "Sigalit": "#8E2C79",
            "Uri": "#299945",
            "Alon": "#E3352E"
        }
        return my_baloon[name]
