
import dearpygui.dearpygui as dpg
import numpy as np

from datetime import datetime


def debug(sender, app_data, user_data, text=''):  
    print('******** DEBUG '+text+'********** ')
    print('Value: ', dpg.get_value(sender))
    print('sender: ', sender)
    print('app_data: ', app_data)
    print('user_data: ', user_data)
    print()

    
def black_image(width, height):  
    return np.zeros((height, width, 3), dtype=np.uint8)


def white_image(width, height):
    white_image = np.ones((height, width, 3), dtype=np.uint8) * 255
    return white_image

def convert_cv_to_dpg(image, width, height):
    
    data = np.flip(image, 2)
    data = data.ravel()
    data = np.asfarray(data, dtype='f')

    texture_data = np.true_divide(data, 255.0)

    return texture_data

