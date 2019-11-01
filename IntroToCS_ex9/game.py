import helper
import car
import board
import sys
import os.path


class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        self.__board = board
        self.__cars = []

    def __car_exist(self, car_name):
        """
        Check if car exist
        :param car_name: string represent car name
        :return: True if exist, False otherwise
        """
        for item in self.__cars:
            if car_name == item.get_name():
                return True
        return False

    def __get_selected_car(self, car_name):
        """
        Get car by car name
        :param car_name: string represent car name
        :return: Car object if exist, False otherwise
        """
        for item in self.__cars:
            if item.get_name() == car_name:
                return item
        return None

    def __exist_in_possible_moves(self, name, move):
        """
        Check if name and move exist in possible moves
        :param name: string represent car name
        :param move: car move key
        :return: True if exist, False otherwise
        """
        possible_moves = self.__board.possible_moves()
        for possible in possible_moves:
            if possible[0] == name and possible[1] == move:
                return True
        return False

    def __validate_input(self, split_input):
        """
        Check validations of input
        :param split_input: input
        :return: String or Error if exist, otherwise None
        """
        if len(split_input) != 2:
            return "Wrong number of arguments"
        elif not self.__car_exist(split_input[0]):
            return "Car ", split_input[0], " does not exist"
        selected_car = self.__get_selected_car(split_input[0])
        if not self.__exist_in_possible_moves(split_input[0], split_input[1]):
            return "The move is not possible for this car"
        requirement = selected_car.movement_requirements(split_input[1])
        if self.__board.cell_content(requirement) != '_':
            return "INVALID: The requirement cell is not empty"
        return None

    def __single_turn(self):
        """
        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        user_input = input("Enter car color and direction: ")
        split_input = user_input.split(',')
        valid = self.__validate_input(split_input)
        if valid is None:
            print(valid)
        else:
            selected_car = self.__get_selected_car(split_input[0])
            if selected_car is None:
                print("Car is INVALID")

            if (selected_car.movement_requirements(split_input[1]) == self.__board.target_location()):
                return True

            move_car = self.__board.move_car(selected_car.get_name(), split_input[1])
            if move_car:
                selected_car.move(split_input[1])

        return False

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        stop = False
        print(self.__board)
        while not stop:
            if self.__single_turn():
                stop = True
            print(self.__board)
        print("Game Over")

    def upload_cars(self, filename):
        """
        Upload cars from json to the game
        :param filename: json filename
        :return: nothing
        """
        car_configs = helper.load_json(filename)
        for item in car_configs.keys():
            new_car = car.Car(item, car_configs[item][0], car_configs[item][1], car_configs[item][2])
            self.__cars.append(new_car)
            self.__board.add_car(new_car)

    def check_args(self, args):
        """
        Check argv
        :param args: arguments list
        :return: String of error if exist, None otherwise
        """
        if len(args) != 1:
            return "Wrong number of arguments"
        elif not os.path.exists(args[0]):
            return "File does not exist"
        return None


if __name__ == "__main__":
    print(sys.argv)
    args = sys.argv[1:]
    rush_game = Game(board.Board())
    args_check = rush_game.check_args(args)
    if args_check != None:
        print(args_check)
    else:
        rush_game.upload_cars(args[0])
        rush_game.play()
