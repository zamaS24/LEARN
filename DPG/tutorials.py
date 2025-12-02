import dearpygui.dearpygui as dpg
import numpy as np
import cv2 as cv
import array
import PIL
import threading 



class Test:
    
    def __init__(self):

        with dpg.window(label="Main window",height=1080, width=720) as pw:
            with dpg.child_window(label="Child window",height=200, width=-1):
                with dpg.group(horizontal=True):
                    self.tf = dpg.add_text("This is just some text", show=True)
                    dpg.add_button(label="Hide text", user_data=False, callback=self.flip) 
                    dpg.add_button(label="show text",user_data=True, callback=self.flip)
        
        with dpg.window(label="another window", height=100, width=100):
            pass

        dpg.set_primary_window(pw, True)


    def flip(self, sender, app_data, user_data):
        dpg.configure_item(self.tf,show=user_data)
        def showinfo():
            print(f"\n----------------------------------------------------")
            print(f"self is :{self}")
            print(f"sender:{sender}")
            print(f"app_data:{app_data}")
            print(f"user_data:{user_data}")
            print(f"----------------------------------------------------\n")
        showinfo()
        
        
class Handler: 
    def __init__(self):

        with dpg.window(label="Main window",height=1080, width=720) as self.pw:

            with dpg.handler_registry(): 
                dpg.add_mouse_move_handler(callback=self.change_text)

        
    def change_text(self, sender, app_data):
                    # will always print 
                    # print("Mouse is moving, this is global handler")
                
                    print({dpg.get_item_state(self.pw)["hovered"]});
       

class Board: 
    def __init__(self):
        
        self.echelle = 50

        with dpg.item_handler_registry(tag="board_handler"):
            dpg.add_item_hover_handler(callback=self.handle_drawlist)
        

        
        with dpg.window(label="Board"):
            with dpg.drawlist(width=510, height=510) as self.drawlist:
                dpg.draw_rectangle([0,0], [500,500], color=[0,0,255], fill=[255,255,255], thickness=2)
                for i in range(0,500,self.echelle):
                    dpg.draw_line([0,i], [500,i], thickness=2, color=[0,0,0])
                    dpg.draw_line([i,0], [i,500], thickness=2, color=[0,0,0,])

                
        dpg.bind_item_handler_registry( self.drawlist, "board_handler")
    

    def handle_drawlist(self, sender, app_data, user_data):
        # callback is fired when there is a hover in the drawlist
        
        self.color_box(dpg.get_drawing_mouse_pos())
        
    def color_box(self, mouse_pos):

        # Getting box coordinates
        [x1,y1] = [int((mouse_pos[0]/self.echelle))*self.echelle, int(mouse_pos[1]/self.echelle)*self.echelle ]
        point1  = [x1,y1]
        point2  = [x1+self.echelle, y1+self.echelle]

        # drawing the box
        dpg.draw_rectangle(point1, point2, parent=self.drawlist, color=[0,0,0], fill=[255,0,0], thickness=2)
        print(f"{[x1,y1]}")


class DpgCv: 

    def __init__(self):
                
        texture_data = None
        vid = None

        dpg.create_context()
        dpg.set_global_font_scale(1.75)

        def show_debugtools(): 
            dpg.show_documentation()
            dpg.show_style_editor()
            dpg.show_debug()
            dpg.show_about()
            dpg.show_metrics()
            dpg.show_font_manager()
            dpg.show_item_registry()


        def task(): 
            global texture_data
            global vid 

            if (dpg.is_item_shown(m_window)):
                ret, frame = vid.read()
                data = np.flip(frame, 2)                    # because the camera data come as BGR and we want is as RGB
                data = data.ravel()                         # flatten camera data to 1d structure
                data = np.asarray(data, dtype='f')          # convert values to 32 bits floats
                texture_data = np.true_divide(data, 255.0)  # normalize image data to prepare for gpu
                
            
        


        dpg.create_viewport(title="Yup testing! ")
        dpg.setup_dearpygui()

        show_debugtools()

        vid = cv.VideoCapture(0)
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

        # main loop 
        while dpg.is_dearpygui_running():
            
              
            if (dpg.is_item_shown(m_window)):
                # normalize image data to prepare for gpu*
                thread = threading.Thread(target=task)
                thread.start()
                dpg.set_value("texture_tag", texture_data)  # Updating the texture tag aka the frame
            
            else: 
                vid.release()
                dpg.set_value("info", "camera  is off")
            
            
            dpg.render_dearpygui_frame()
            


        vid.release()
        dpg.destroy_context()


class NodeEditor(): 
    def __init__(self): 
        pass  


# Test of the VideoCaputre with a frame in dearpygui.
# DpgCv()


