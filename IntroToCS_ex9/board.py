DIRECTIONS = 'u', 'd', 'r', 'l'
BOARD_SIZE = 7
TARGET = (3, 7)
EMPTY_CELL = None


class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        result = []
        for i in range(BOARD_SIZE):
            ln = []
            for j in range(BOARD_SIZE):
                ln.append(EMPTY_CELL)
            result.append(ln)
        self.__board = result
        self.__cars = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        result = ""
        for row in range(len(self.__board)):
            for col in range(len(self.__board)):
                if self.__board[row][col] == EMPTY_CELL:
                    result += "_"
                else:
                    result += self.__board[row][col]
                result += " "
            result += "\n"
        return result

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        result = []
        for i in range(len(self.__board)):
            for j in range(len(self.__board)):
                result.append((i, j))
        if len(result) != 0:
            result.append(TARGET)
        return result

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        # From the provided example car_config.json file, the return value could be
        # [('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        result = []
        for item in self.__cars:
            moves = item.possible_moves()
            for move in moves.keys():
                result.append((item.get_name(), move, moves[move]))
        return result

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return TARGET

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        if coordinate[0] < len(self.__board) and coordinate[1] < len(self.__board):
            return self.__board[coordinate[0]][coordinate[1]]

    def __car_exist(self, one_car):
        """
        Function that check if car exist in
            cars list
        :param one_car:  string represent car name
        :return: True if exist, False otherwise
        """
        for item in self.__cars:
            if item.get_name() == one_car.get_name():
                return True
        return False

    def add_car(self, one_car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        if self.__car_exist(one_car):
            return False

        car_coordinates = one_car.car_coordinates()
        if not self.__valid_coordinates(car_coordinates[0]):
            return False
        if not self.__valid_coordinates(car_coordinates[-1]):
            return False

        for coordinate in car_coordinates:
            if self.__board[coordinate[0]][coordinate[1]] != EMPTY_CELL:
                return False

        for coordinate in car_coordinates:
            self.__board[coordinate[0]][coordinate[1]] = one_car.get_name()

        self.__cars.append(one_car)

    def __get_car(self, name):
        """
        Get car by name
        :param name:string represent car name
        :return: Car object if exist, None otherwise
        """
        for item in self.__cars:
            if item.get_name() == name:
                return item

    def __valid_coordinates(self, coordinates):
        """"
        :param coordinates: tuple
        :return False if out of bounds. otherwise None
        """
        if coordinates == TARGET:
            return True

        for i in range(2):
            if coordinates not in self.cell_list():
                print("coordinate is out of bound")
                return False

        if self.cell_content(coordinates) != EMPTY_CELL:
            print("cannot move, there is car there")
            return False

        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        selected_car = self.__get_car(name)
        if selected_car is None:
            print("Car does not exist")
            return False

        requirement = selected_car.movement_requirements(movekey)

        if requirement == TARGET:
            return True

        car_represent = selected_car.car_coordinates()
        if not self.__valid_coordinates(requirement):
            return False

        try:
            if movekey == 'u':
                self.__board[car_represent[0][0] - 1][car_represent[0][1]] = name
                self.__board[car_represent[-1][0]][car_represent[-1][1]] = EMPTY_CELL
            elif movekey == 'd':
                self.__board[car_represent[0][0]][car_represent[0][1]] = EMPTY_CELL
                self.__board[car_represent[-1][0] + 1][car_represent[-1][1]] = name
            elif movekey == 'l':
                self.__board[car_represent[0][0]][car_represent[0][1] - 1] = name
                self.__board[car_represent[-1][0]][car_represent[-1][1]] = EMPTY_CELL
            elif movekey == 'r':
                self.__board[car_represent[0][0]][car_represent[0][1]] = EMPTY_CELL
                self.__board[car_represent[-1][0]][car_represent[-1][1] + 1] = name
        except:
            print("Move fail")
            return False

        return True