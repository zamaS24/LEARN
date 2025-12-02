import dearpygui.dearpygui as dpg
from board import Board


class TicTacToe: 
    def __init__(self):

        CELLSIZE = 100
        ROWSIZE = 3

        self.main_window = None
        self._mount_main_window()
        self.board = Board(
            CELLSIZE, ROWSIZE,
            parent=self.main_window,
            board_dimensions=[305,305],
            board_window_dimensions=[320,320]
        )
        self.board._mount_board_window() #this is wrong we should not name it with _

        

    # function to mount window to the viewport and 
    # set it as main window
    def _mount_main_window(self):

        with dpg.window(
        width=750, height=750,
        label="Game"
        ) as self.main_window:
            pass
        
        dpg.set_primary_window(self.main_window, True)

