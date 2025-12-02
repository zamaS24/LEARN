import dearpygui.dearpygui as dpg 


class Board:

    def __init__(self,
    cell_size, row_size, parent=None, 
    board_dimensions=None,
    board_window_dimensions = None
    ):
        self.board_tag = None
        self.cell_size = cell_size
        self.row_size= row_size
        self.parent=parent

        self.board_dimensions = board_dimensions
        self.board_window_dimensions = board_window_dimensions

        self.drawList = None

        # attributo that maps each dpg rectangle to it's position
        self.cell_idx = []

        # mount the board to the parent window
        if parent is not None: 
            self._mount_board_window()

        
 
    # function to mount a board window to a parent window
    def _mount_board_window(self):
        with dpg.child_window(
            width=self.board_window_dimensions[0],
            height=self.board_window_dimensions[1], 
            parent=self.parent,
            no_scrollbar=True,
            pos=[325,10]
        )as self.board_tag:
            

            self.drawList = dpg.add_drawlist(
            self.board_dimensions[0],
            self.board_dimensions[1]
            )

            # Draw the boxes
            # TODO make it automatic for any given number of row-col size
            c0 = dpg.draw_rectangle(pmin=[0,0],     pmax=[100,100], parent=self.drawList)
            c1 = dpg.draw_rectangle(pmin=[101,0],   pmax=[201,100], parent=self.drawList)
            c2 = dpg.draw_rectangle(pmin=[202,0],   pmax=[302,100], parent=self.drawList)
            c3 = dpg.draw_rectangle(pmin=[0,101],   pmax=[100,201], parent=self.drawList)
            c4 = dpg.draw_rectangle(pmin=[101,101], pmax=[201,201], parent=self.drawList)
            c5 = dpg.draw_rectangle(pmin=[202,101], pmax=[302,201], parent=self.drawList)
            c6 = dpg.draw_rectangle(pmin=[0,202],   pmax=[100,302], parent=self.drawList)
            c7 = dpg.draw_rectangle(pmin=[101,202], pmax=[201,302], parent=self.drawList)
            c8 = dpg.draw_rectangle(pmin=[202,202], pmax=[302,302], parent=self.drawList)

            item_to_append = [c0,c1,c2,c3,c4,c5,c6,c7,c8]
            self.cell_idx.extend(item_to_append)


    def draw_X(self, position): 
        dpg.configure_item(self.cell_idx[position], )

    def draw_O(self, position): 
        pass

    def _reset_board(self, position): 
        if self.board_tag is not None: 
            dpg.delete_item(self.board_tag)

        self._mount_board_window(self.board)
    

    # unmount window board from parent window
    def unmount_board(self): 
        dpg.delete_item(self.board_tag)
        


    

