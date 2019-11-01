from screen import Screen
import sys
from asteroid import Asteroid
from ship import Ship
from torpedo import Torpedo

DEFAULT_ASTEROIDS_NUM = 5
MAX_TORPEDO = 10
MAX_SPECIAL_TORPEDO = 5
SCORES = {
    3: 20,
    2: 50,
    1: 100
}
MESSAGE_TITLE = "YOU HAD ONE JOB!"
MESSAGE = "The asteroid are not chocolates, avoid them"

class GameRunner:
    def __init__(self, asteroids_amount):
        """
        :param .__screen: the screen of the game

        #### NOTE: the follow parameter are unused, but we left it here so it
        wouldn't fall in automatic tests. ###

        :param .__screen_max_x: the max vertical coordination of the screen.
        :param .__screen_max_y: the max horizontal coordination of the screen.
        :param .__screen_min_x: the min vertical coordination of the screen.
        :param .__screen_min_y: the min horizontal coordination of the screen.

        :param .__current_ship: ship object - the ship of the game.
        :param .__asteroid_list: list of all the asteroid in the game
        :param .__torpedo_list: a list of all the torpedoes in the game.
        :param .__score: the score the player got.
        """
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__current_ship = Ship()
        self.__asteroid_list = []
        self.__torpedo_list = []
        self.__score = 0

        self._init_asteroid_start(asteroids_amount=asteroids_amount)

    def run(self):
        """
        runs the whole game
        """
        self._do_loop()
        self.__screen.start_screen()

    def _gain_score(self, asteroid_size):
        """
        this function updated the score by the size of the bombarded asteroid.
        :param asteroid_size: the size of the asteroid
        """
        if(asteroid_size in SCORES.keys()):
            self.__score += SCORES[asteroid_size]

        self.__screen.set_score(self.__score)

    def _do_loop(self):
        """
        takes a game loop.
        """
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        """
        makes a game loop.
        handles all the objects one by one using some assist functions.
        ends the game in the relevant situation.
        :return:
        """

        # Handle ship
        self._handle_ship()

        # Draw and move asteroids
        self._handle_asteroid()

        # Handle torpedo
        self._handle_torpedo()

        # Handle teleport
        self._handle_teleport()

        # Handle end game
        self._handle_end_game()

    def _handle_end_game(self):
        """
        ends the game
        """
        if self.__screen.should_end() or self.__current_ship.get_life() == 0:
            self.__screen.end_game()

    def _handle_teleport(self):
        """
        teleport ship
        """
        if self.__screen.is_teleport_pressed():
            self.__current_ship.set_random_location()

    def _handle_asteroid(self):
        """
        draws the asteroids.
        takes care of the different interactions between asteroids
        and other objects - intersections with ship and torpedo.
        makes the asteroids move.
        """
        for asteroid_item in self.__asteroid_list:
            self.__screen.draw_asteroid(asteroid=asteroid_item,
                                        x=asteroid_item.get_location_x(),
                                        y=asteroid_item.get_location_y())
            asteroid_item.move()

            # Intersections
            self._asteroid_ship_intersection(asteroid_item=asteroid_item)
            self._asteroid_torpedo_intersection(asteroid_item=asteroid_item)

    def _asteroid_ship_intersection(self, asteroid_item):
        """"
        handles the ship and asteroid interaction.
        """
        # Asteroid interact ship
        if asteroid_item.has_intersection(obj=self.__current_ship):
            self.__current_ship.take_life()
            self.__screen.remove_life()
            self._break_asteroid(asteroid_item=asteroid_item,
                                 obj=self.__current_ship)
            self.__screen.show_message(title=MESSAGE_TITLE,
                                       msg=MESSAGE)

    def _asteroid_torpedo_intersection(self, asteroid_item):
        """
        deals with asteroid and torpedo intersection.
        :param asteroid_item:
        """
        # Asteroid interact torpedo
        for torpedo_item in self.__torpedo_list:
            if asteroid_item.has_intersection(obj=torpedo_item):
                self._gain_score(asteroid_item.get_size())
                self._break_asteroid(asteroid_item=asteroid_item,
                                     obj=torpedo_item,
                                     special=torpedo_item.is_special())

    def _handle_ship(self):
        """
        handles the ship -
        draws the ship
        controls the speed of the ship
        controls the direction of the ship
        """
        self.__screen.draw_ship(x=self.__current_ship.get_location_x(),
                                y=self.__current_ship.get_location_y(),
                                heading=self.__current_ship.get_angle())
        self.__current_ship.move()
        if self.__screen.is_up_pressed():
            self.__current_ship.faster()
        if self.__screen.is_left_pressed():
            self.__current_ship.change_left_angle()
        if self.__screen.is_right_pressed():
            self.__current_ship.change_right_angle()

    def _special_torpedo_count(self):
        """"
        counted the number of the special torpedoes.
        """
        count = 0
        for item in self.__torpedo_list:
            if item.is_special():
                count += 1
        return count

    def _handle_torpedo(self):
        """
        handles the torpedo -
        draws the torpedo
        defines a special torpedo and handles with it.
        insures that the there is a legal number of torpedoes
        remove torpedo after 200 iterations of "game loop".
        """
        if self.__screen.is_space_pressed() and \
                len(self.__torpedo_list) < MAX_TORPEDO:
            self._launch_torpedo(special=False)

        if self.__screen.is_special_pressed() and \
                self._special_torpedo_count() < MAX_SPECIAL_TORPEDO:
            self._launch_torpedo(special=True)

        current_torpedo_list = self.__torpedo_list
        torpedo_copy = current_torpedo_list[:]

        for torpedo_item in torpedo_copy:
            if not torpedo_item.is_special():
                torpedo_item.take_a_life()
            if torpedo_item.get_life() == 0:
                self.__screen.unregister_torpedo(torpedo=torpedo_item)
                current_torpedo_list.remove(torpedo_item)
            else:
                self.__screen.draw_torpedo(torpedo=torpedo_item,
                                           x=torpedo_item.get_location_x(),
                                           y=torpedo_item.get_location_y(),
                                           heading=torpedo_item.get_angle())
                torpedo_item.move()

    def _launch_torpedo(self, special):
        """
        creates an torpedo and register it.
        appends the new torpedo to the total list of the torpedoes.
        """
        new_torpedo = Torpedo(current_ship=self.__current_ship,
                              special=special)
        self.__screen.register_torpedo(torpedo=new_torpedo)
        self.__torpedo_list.append(new_torpedo)

    def _init_asteroid_start(self, asteroids_amount):
        """
        launch new asteroid.
        :param asteroids_amount:
        """
        for i in range(asteroids_amount):
            new_asteroid = Asteroid()
            self.__asteroid_list.append(new_asteroid)
            self.__screen.register_asteroid(asteroid=new_asteroid,
                                            size=new_asteroid.get_size())

    def _break_asteroid(self, asteroid_item, obj, special=False):
        """
        breaks the asteroid to two pieces.
        :param asteroid_item: the specific asteroid
        :param obj: the object that interact with the asteroid.
        """
        if not special and type(obj) == Asteroid:
            for broken_asteroid in asteroid_item.break_asteroid(obj=obj):
                self.__screen.register_asteroid\
                    (asteroid=broken_asteroid,size=broken_asteroid.get_size())
                self.__asteroid_list.append(broken_asteroid)

        self.__screen.unregister_asteroid(asteroid=asteroid_item)
        self.__asteroid_list.remove(asteroid_item)


def main(amount):
    """
    :param amount:
    runs all the game.
    """
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
