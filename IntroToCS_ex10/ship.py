from game_object import GameObject
import math
import random

SHIP_RADIUS = 1
START_LIFE = 3


class Ship(GameObject):
    def __init__(self):
        """
        :param ._location_x: the vertical location of the ship.
        :param ._location_y: the horizontal location of the ship.
        :param ._speed_x: the vertical speed of the ship.
        :param ._speed_y: the horizontal speed of the ship.
        :param ._angle: the angle of the ship.
        :param ._life: how many losses left for the ship.
        :param ._radius: the radius of the ship.
        """
        GameObject.__init__(self)
        self.set_random_location()
        self._angle = 0
        self._life = START_LIFE
        self._radius = SHIP_RADIUS

    def get_angle(self):
        """
        :return: the ship's angle.
        """
        return self._angle

    def change_right_angle(self):
        """
        this function handles with right press of the user.
        """
        self._angle = self._angle - 7

    def change_left_angle(self):
        """
        this function handles with left press of the user.
        """
        self._angle = self._angle + 7

    def faster(self):
        """
        this function speeds up the ship.
        """
        rad_angle = (math.pi / 180) * self._angle
        self._speed_x = self._speed_x + math.cos(rad_angle)
        self._speed_y = self._speed_y + math.sin(rad_angle)

    def take_life(self):
        """
        this function takes off a life from the ship. For use if the ship
        was part of intersection.
        """
        self._life -= 1

    def get_life(self):
        """
        :return: the parameter 'life'.
        """
        return self._life

    def set_random_location(self):
        """
        puts the ship in a random spot on the screen.
        """
        self._location_x = \
            random.randrange(self._screen_min_x, self._screen_max_x)
        self._location_y = \
            random.randrange(self._screen_min_y, self._screen_max_y)

