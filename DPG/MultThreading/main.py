import cv2 as cv
import dearpygui.dearpygui as dpg 
import numpy as np 
import threading 

texture_data = None
vid = cv.VideoCapture(0)

dpg.create_context()
dpg.set_global_font_scale(1.75)

def show_debugtools(): 
    # dpg.show_documentation()    # not important
    dpg.show_style_editor()     # important for syles testing
    # dpg.show_debug()            # not important documentation 
    # dpg.show_about()            # Not important 
    dpg.show_metrics()          # important has moouse position
    # dpg.show_font_manager()     # not really important if you are not testing different fonts
    dpg.show_item_registry()    # I guess important




def async_task(): 
    global texture_data
    global vid 

    
    try: 
        ret, frame = vid.read()
        data = np.flip(frame, 2)                    # because the camera data come as BGR and we want is as RGB
        data = data.ravel()                         # flatten camera data to 1d structure
        data = np.asarray(data, dtype='f')          # convert values to 32 bits floats
        texture_data = np.true_divide(data, 255.0)  # normalize image data to prepare for gpu
    except: 
        pass
        
    



dpg.create_viewport(title="Multi Threading")
dpg.setup_dearpygui()

show_debugtools()


ret, frame = vid.read()

frame_width = vid.get(cv.CAP_PROP_FRAME_WIDTH)
frame_height = vid.get(cv.CAP_PROP_FRAME_HEIGHT)
video_fps = vid.get(cv.CAP_PROP_FPS)

data = np.flip(frame, 2)                    # because the camera data come as BGR and we want is as RGB
data = data.ravel()                         # flatten camera data to 1d structure
data = np.asarray(data, dtype='f')          # convert values to 32 bits floats
texture_data = np.true_divide(data, 255.0)  # normalize image data to prepare for gpu


with dpg.texture_registry(show=True) as tr: 
    dpg.add_raw_texture(
        frame_width,
        frame_height,
        texture_data,
        format=dpg.mvFormat_Float_rgb, 
        tag="texture_tag", 
        label="video_frame"
    )

    
with dpg.window(label="Example window") as m_window:
    dpg.add_image("texture_tag")
    
with dpg.window():
    dpg.add_text("camera is on", tag="info")


# dpg.is_item_toggled_open
# below replaces, start_dearpygui()
dpg.show_viewport()


# main loop (main thread) ?
while dpg.is_dearpygui_running():
        
    if (dpg.is_item_shown(m_window)):
        # multithreading you feel me bruh?            
        threading.Thread(target=async_task).start()
        dpg.set_value("texture_tag", texture_data) 
    
    else: 
        dpg.set_value("info", "camera  is off")
    
    dpg.render_dearpygui_frame()
    

vid.release()
dpg.destroy_context()



