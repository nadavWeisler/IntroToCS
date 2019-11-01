from game_object import GameObject
import math
import random
import copy

DEFAULT_ASTEROIDS_NUM = 5
BASE_ASTEROID_SIZE = 3


class Asteroid(GameObject):
    def __init__(self):
        """
        :param ._location_x: the vertical location of the torpedo.
        :param ._location_y: the horizontal location of the torpedo.
        :param ._speed_x: the vertical speed of the torpedo.
        :param ._speed_y: the horizontal speed of the torpedo.
        :param ._size: the angle of the torpedo.
        :param ._radius: the radius of the asteroid.
        """
        GameObject.__init__(self)
        asteroid_options = self._create_asteroid_options()
        self._speed_x = random.choice(asteroid_options)
        self._speed_y = random.choice(asteroid_options)
        self._location_x = \
            random.randrange(self._screen_min_x, self._screen_max_x)
        self._location_y = \
            random.randrange(self._screen_min_x, self._screen_max_y)
        self._size = BASE_ASTEROID_SIZE
        self._radius = self._size * 10 - 5

    def _create_asteroid_options(self):
        """
        :return: the asteroids speeds options
        """
        range_default_asteroid_num = list(range(DEFAULT_ASTEROIDS_NUM))
        result = range_default_asteroid_num[:]
        for i in range_default_asteroid_num:
            result.append(i * -1)
        while 0 in result:
            result.remove(0)
        return result

    def _create_broken_asteroid_from_this(self, speed_x, speed_y):
        new_asteroid1 = Asteroid()
        new_asteroid1._location_x = self._location_x
        new_asteroid1._location_y = self._location_y
        new_asteroid1._speed_x = speed_x
        new_asteroid1._speed_y = speed_y
        new_asteroid1._size = self.get_size() - 1

        new_asteroid2 = copy.copy(new_asteroid1)
        new_asteroid2._speed_x *= -1
        new_asteroid2._speed_y *= -1

        return (new_asteroid1, new_asteroid2)

    def _get_broke_asteroid_speed(self, obj):
        """
        :param obj:  can be a torpedo or a ship.
        :return: the speed of thw spitted asteroids.
        """
        x_speed = (obj.get_speed_x() + self._speed_x) / (
            math.sqrt((self._speed_x ** 2) + (self._speed_y ** 2)))
        y_speed = (obj.get_speed_y() + self._speed_y) / (
            math.sqrt((self._speed_x ** 2) + (self._speed_y ** 2)))
        return (x_speed, y_speed)

    def get_size(self):
        """
        :return: the size of the asteroid.
        """
        return self._size

    def has_intersection(self, obj):
        """
        :param obj: can be a torpedo or a ship.
        :return: boolean - if there was intersection or not.
        """
        distance = math.sqrt(((obj.get_location_x() - self._location_x) ** 2) +
                             ((obj.get_location_y() - self._location_y) ** 2))
        return (distance <= self.radius() + obj.radius())

    def break_asteroid(self, obj):
        """
        :param obj:  can be a torpedo or a ship.
        breaks the asteroid into two pieces.
        :return: tuple of the new asteroids.
        """
        if self._size > 1:
            speed = self._get_broke_asteroid_speed(obj=obj)
            return self._create_broken_asteroid_from_this(speed_x=speed[0],
                                                          speed_y=speed[1])
        else:
            return ()
