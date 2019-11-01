from screen import Screen


class GameObject:
    """"
    אWe created this module based on the mutual properties of the objects in
    the game.
    """
    def __init__(self):
        """
        :param ._location_x: the vertical location of the object.
        :param ._location_y: the horizontal location of the object.
        :param ._speed_x: the vertical speed of the object.
        :param ._speed_y: the horizontal speed of the object.
        :param ._screen_max_x: the max vertical coordination of the screen.
        :param ._screen_max_y: the max horizontal coordination of the screen.
        :param ._screen_min_x: the min vertical coordination of the screen.
        :param ._screen_min_y: the min horizontal coordination of the screen.
        :param ._radius: the radius of the object.
        """
        self._location_x = 0
        self._location_y = 0
        self._speed_x = 0
        self._speed_y = 0
        self._screen_max_x = Screen.SCREEN_MAX_X
        self._screen_max_y = Screen.SCREEN_MAX_Y
        self._screen_min_x = Screen.SCREEN_MIN_X
        self._screen_min_y = Screen.SCREEN_MIN_Y
        self._radius = 0

    def get_location_x(self):
        """
        :return: returns the vertical location of the object.
        """
        return self._location_x

    def get_location_y(self):
        """
        :return: returns the horizontal location of the object.
        """
        return self._location_y

    def get_speed_x(self):
        """
        :return: returns the vertical speed of the object.
        """
        return self._speed_x

    def get_speed_y(self):
        """
        :return: returns the horizontal speed of the object.
        """
        return self._speed_y

    def radius(self):
        """"
        :return: return object radius
        """
        return self._radius

    def move(self):
        """
        this function moves the object based on an equation,
        and information about the object's location and speed.
        """
        delta_x = self._screen_max_x - self._screen_min_x
        delta_y = self._screen_max_y - self._screen_min_y
        self._location_x = (self._speed_x + self._location_x -
                          self._screen_min_x) % delta_x + self._screen_min_x
        self._location_y = (self._speed_y + self._location_y -
                          self._screen_min_y) % delta_y + self._screen_min_y
