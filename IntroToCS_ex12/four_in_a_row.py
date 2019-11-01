from ex12.menu_gui import MenuGui
from ex12.screen_gui import ScreenGui
from tkinter import *

def run_single_game():
    stop = False
    while not stop:
        root = Tk()
        player1_var = StringVar()
        player2_var = StringVar()
        app = MenuGui(root, player1_var, player2_var)
        root.mainloop()
        root.destroy()
        root2 = Tk()
        game_app = ScreenGui(root2, app.player1, app.player2)
        root2.mainloop()
        root2.destroy()
        if not game_app.new_game_start:
            stop = True


if __name__ == '__main__':
    run_single_game()
