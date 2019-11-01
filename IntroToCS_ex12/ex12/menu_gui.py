from .player import Player
from tkinter import Radiobutton, Button, Label, Tk

class MenuGui:
    def __init__(self, master, player1_var, player2_var):
        self.master = master
        self.player1_var = player1_var
        self.player2_var = player2_var

        master.title('Welcome to Connect Four')

        master.configure(background='white')

        label_player1 = Label(master,
                              text="Player 1: ",
                              font=("Helvetica", 16),
                              background='white',
                              fg='black')

        player1_manual = Radiobutton(master,
                                     text='Manual',
                                     variable=player1_var,
                                     value=1)

        player1_manual.select()

        player1_ai1 = Radiobutton(master, text='Easy AI', variable=player1_var,
                                  value=2)

        player1_ai1.deselect()

        player1_ai2 = Radiobutton(master, text='Normal AI',
                                  variable=player1_var,
                                  value=3)

        player1_ai2.deselect()

        player1_ai3 = Radiobutton(master, text='Hard AI', variable=player1_var,
                                  value=4)

        player1_ai3.deselect()

        label_player1.grid(row=0)

        player1_manual.grid(column=1, row=0)

        player1_ai1.grid(column=2, row=0)

        player1_ai2.grid(column=3, row=0)

        player1_ai3.grid(column=4, row=0)

        # labeling player 2 menu
        label_player2 = Label(master,
                              text="Player 2: ",
                              font=("Helvetica", 16),
                              background='white',
                              fg='black')

        # creating player 2 menu, including
        player2_manual = Radiobutton(master,
                                     text='Manual',
                                     variable=player2_var,
                                     value=1)
        player2_manual.select()
        player2_ai1 = Radiobutton(master,
                                  text='Easy AI',
                                  variable=player2_var,
                                  value=2)
        player2_ai1.deselect()
        player2_ai2 = Radiobutton(master,
                                  text='Normal AI',
                                  variable=player2_var,
                                  value=3)
        player2_ai2.deselect()
        player2_ai3 = Radiobutton(master,
                                  text='Hard AI',
                                  variable=player2_var,
                                  value=4)
        player2_ai3.deselect()

        # player 2 menu locating
        label_player2.grid(row=1)
        player2_manual.grid(column=1, row=1)
        player2_ai1.grid(column=2, row=1)
        player2_ai2.grid(column=3, row=1)
        player2_ai3.grid(column=4, row=1)

        # creating
        button = Button(master,
                        text="GO!",
                        command=self._start_game)

        button.grid(row=3)

    def _start_game(self):
        player1_var = self.player1_var.get()
        player2_var = self.player2_var.get()
        self.player1 = self._get_player_from_var(player1_var)
        self.player2 = self._get_player_from_var(player2_var,
                                                 self.player1.get_name())
        self.master.quit()

    def _get_player_from_var(self, var, pre_player=None):
        ai = False
        level = None
        if var == '2':
            ai = True
            level = 1
        elif var == '3':
            ai = True
            level = 3
        elif var == '4':
            ai = True
            level = 5
        return Player(exist_player=pre_player,
                      ai=ai,
                      level=level)
