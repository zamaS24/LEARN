import numpy as np
from utils import debug, black_image, convert_cv_to_dpg

from Node import FrameNode

def _callback_link(sender, app_data, user_data):
    debug(sender, app_data, user_data)
    pass

def _callback_delink(sender, app_data, user_data): 
    debug(sender, app_data, user_data)
    pass


def callback_add_frame_node(sender, app_data, user_data):
    # debug(sender, app_data, user_data)
    

    black_img = black_image(100, 100)
    black_texture = convert_cv_to_dpg(black_img, 100, 100)

    frame_node = FrameNode("tag_node_editor", 100, 100, black_texture)
    

def callback_test(sender, app_data, user_data, Node_obj=None):
    pass



