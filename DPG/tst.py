import dearpygui.dearpygui as dpg
import cv2 as cv
import numpy as np
import PIL 






class Vision:
    def __init__(self): 
        pass





# Tester comment avoir les coordonnés du box selon les coordonnées de la souris
class Echelle: 
    echelle = 10

    mouse_pos = [67.5,45.5]

    point1  = [int((mouse_pos[0]/echelle))*echelle, int(mouse_pos[1]/echelle)*echelle ]
    point2  = [int(mouse_pos[0]/echelle)*echelle+echelle, int(mouse_pos[1]/echelle)*echelle+echelle]


    print(f"point 1 coordinates : {point1}")
    print(f"point 2 coordinates : {point2}")