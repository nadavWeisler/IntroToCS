from game_object import GameObject
import math

TORPEDO_RADIUS = 4
TORPEDO_MAX_LIFE = 200
TORPEDO_SPECIAL_MAX_LIFE = 150


class Torpedo(GameObject):
    def __init__(self, current_ship, special=False):
        """
        :param ._location_x: the vertical location of the torpedo.
        :param ._location_y: the horizontal location of the torpedo.
        :param ._speed_x: the vertical speed of the torpedo.
        :param ._speed_y: the horizontal speed of the torpedo.
        :param ._angle: the angle of the torpedo.
        :param ._special: boolean parameter which tells if the torpedo is
        special or not.
        :param ._life: how many iterations left for the torpedo to live.
        """
        GameObject.__init__(self)
        self._location_x = current_ship.get_location_x()
        self._location_y = current_ship.get_location_y()
        self._speed_x = self._get_torpedo_speed_x\
            (current_ship.get_speed_x(), current_ship.get_angle())
        self._speed_y = self._get_torpedo_speed_y\
            (current_ship.get_speed_y(), current_ship.get_angle())
        self._angle = current_ship.get_angle()
        self._special = special
        self._radius = TORPEDO_RADIUS

        if special:
            self._life = TORPEDO_SPECIAL_MAX_LIFE
        else:
            self._life = TORPEDO_MAX_LIFE

    def _get_rad_angle(self, angle):
        """

        :param angle:
        :return:
        """
        return angle * math.pi / 180

    def _get_torpedo_speed_x(self, speed_x, angle):
        """

        :param speed_x:
        :param speed_y:
        :param angle:
        :return:
        """
        return speed_x + 2 * math.sin(self._get_rad_angle(angle))

    def _get_torpedo_speed_y(self, speed_y, angle):
        """

        :param speed_x:
        :param speed_y:
        :param angle:
        :return:
        """
        return speed_y + 2 * math.cos(self._get_rad_angle(angle))

    def get_angle(self):
        """
        :return: the angle of the torpedo.
        """
        return self._angle

    def is_special(self):
        """
        :return: True if the torpedo is special, False if not.
        """
        return self._special

    def get_life(self):
        """
        :return: the parameter "life".
        """
        return self._life

    def take_a_life(self):
        """
        :return: take 1 'life' off the torpedo.
        """
        self._life -= 1

