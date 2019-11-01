from tkinter import messagebox, Label, Canvas, StringVar, W, Button, ALL
from .game import Game
from .ai import AI

COLUMNS_COUNT = 7
ROW_COUNT = 6
GRID_COLOR = "#F5B763"
ELEMENT_SIZE = 50
GRID_BORDER = 3
BACKGROUND_COLOR_WHITE = "#FFFFFF"
BACKGROUND_COLOR_BROWN = "#8F5B15"


class ScreenGui:
    game_on = False

    def __init__(self, master, player1, player2):
        """
        :param master: the base of the graphic screen.
        :param player1: the first player.
        :param player2: the second player.
        """
        self.master = master
        self.player1 = player1
        self.player2 = player2
        self.new_game_start = False

        # the title of the screen
        master.title('Connect Four')

        master.configure(background=BACKGROUND_COLOR_BROWN)

        # the title the inner screen
        title_label = Label(master,
                      text="Connect Four - " +
                           self.player1.get_name() + " vs " +
                           self.player2.get_name(),
                      font=("Helvetica", 30),
                      background=BACKGROUND_COLOR_BROWN,
                      fg=BACKGROUND_COLOR_WHITE)

        title_label.grid(row=0)

        self.current_player = StringVar(self.master, value="")
        self.current_player_label = Label(self.master,
                                          textvariable=self.current_player,
                                          background=BACKGROUND_COLOR_BROWN,
                                          fg=BACKGROUND_COLOR_WHITE,
                                          anchor=W)
        self.current_player_label.grid(row=1)

        self.canvas = Canvas(master,
                             width=200,
                             height=50,
                             background=BACKGROUND_COLOR_WHITE,
                             highlightthickness=0)

        self.canvas.grid(row=2)

        button = Button(master,
                        text="New Game!",
                        command=self._new_game_btn)

        button.grid(row=3)

        self.canvas.bind('<Button-1>', self._canvas_click)
        self.new_game()

    def draw(self):
        """
        draws a disc on the board.
        """
        for column in range(COLUMNS_COUNT):
            for row in range(ROW_COUNT):
                if row >= COLUMNS_COUNT:
                    continue

                fill = self.fill_the_cell(column, row)

                self.put_graphic_disc(column, row, fill)

    def put_graphic_disc(self, column, row, fill):
        """
        draws the oval itself on the screen.
        :param column: the index of the desired column.
        :param row: the index of the desired row.
        :param fill: the color to fill the circle that presets the disc.
        """
        x0 = int(column) * ELEMENT_SIZE
        y0 = int(row) * ELEMENT_SIZE
        x1 = (int(column) + 1) * ELEMENT_SIZE
        y1 = (int(row) + 1) * ELEMENT_SIZE
        self.canvas.create_oval(x0 + 2,
                                self.canvas.winfo_height() - (y0 + 2),
                                x1 - 2,
                                self.canvas.winfo_height() - (y1 - 2),
                                fill=fill, outline=GRID_COLOR)

    def fill_the_cell(self, column, row):
        """
        :param column: the index of the desired column.
        :param row: the index of the desired row.
        :return: the fill of the cell.
        """
        fill = GRID_COLOR
        if self.game.get_cell_value(row, column) == \
                self.game.get_players()[0].get_player_number():
            fill = self.game.get_players()[0].get_player_color()
        elif self.game.get_cell_value(row, column) == \
                self.game.get_players()[1].get_player_number():
            fill = self.game.get_players()[1].get_player_color()
        return fill

    def draw_board(self):
        """
        draws the board on the canvas.
        """
        x0, x1 = 0, self.canvas.winfo_width()
        for ROW in range(1, COLUMNS_COUNT):
            y = ROW * ELEMENT_SIZE
            self.canvas.create_line(x0, y, x1, y, fill=GRID_COLOR)

        y0, y1 = 0, self.canvas.winfo_height()
        for column in range(1, ROW_COUNT):
            x = column * ELEMENT_SIZE
            self.canvas.create_line(x, y0, x, y1, fill=GRID_COLOR)

    def drop(self, column):
        """
        :param column: the desired column.
        :return: one turn function of Game object.
        """
        return self.game.one_turn(column)

    def new_game(self):
        """
        starts a new game
        """

        self.game = Game(self.player1, self.player2)

        ai1 = None
        ai2 = None
        if self.player1.player_is_ai():
            ai1 = AI(self.game, self.player1, self.player1.get_player_level())
        if self.player2.player_is_ai():
            ai2 = AI(self.game, self.player2, self.player2.get_player_level())

        self.game.append_ai(ai1, ai2)
        self.canvas.delete(ALL)
        self.canvas.config(width=ELEMENT_SIZE * COLUMNS_COUNT,
                           height=ELEMENT_SIZE * ROW_COUNT)
        self.master.update()
        self.draw_board()
        self.draw()

        self._update_current_player()

        self.game_on = True
        if self.game.current_player_is_ai():
            self._ai_move()

    def _update_current_player(self):
        """
        :return: updates the current player.
        """
        self.current_player.set('Current player: ' +
                                self.game.get_current_player_object().get_name())

    def _ai_move(self):
        """
        makes an ai move. This is an recursive function.
        """
        if not self.game_on:
            return
        if self.game.get_winner() is not None:
            return

        self.game.one_turn_ai()
        self.draw()
        self._update_current_player()

        if self.game.get_winner() is not None:
            self._do_game_over()
        else:
            if self.game.current_player_is_ai():
                self._ai_move()

    def _do_game_over(self):
        """
        end the whole iteration of the game.
        """
        if self.game.get_winner() == 0:
            text = 'DRAW!'
            title = "No winner..."
        else:
            winner = self.game.get_current_player_object().get_name()
            text = winner + ' won!'
            title = "WINNER!"

        messagebox.showinfo(title, text)

    def _canvas_click(self, event):
        """
        doing the process that click on the borad doing - droppimg and
        drawing. Finish the game if needed.
        """
        if not self.game_on:
            return
        if self.game.get_winner():
            return

        col = event.x // ELEMENT_SIZE

        if self.game.validate_col(col):
            self.drop(col)
            self.draw()
            self._update_current_player()

        if self.game.get_winner():
            self._do_game_over()
        else:
            if self.game.current_player_is_ai():
                self._ai_move()

    def _new_game_btn(self):
        """
        supporter for new game generator
        """
        self.new_game_start = True
        self.master.quit()
