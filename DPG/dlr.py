# !\usr\bin\env\python3 

import dearpygui.dearpygui as dpg 

def show_debugtools(): 
    dpg.show_style_editor()
    dpg.show_debug()
    dpg.show_item_registry()


dpg.create_context()
dpg.set_global_font_scale(1.75)
dpg.create_viewport(title="Main App")


# NOTE: you can't just fix this shit right here okay?
# thank me later man okay?
# I really don't know why hahah see you later by the way 

class App(object): 
    
    def __init__(self): 

        self.texture_tag = None

        with dpg.window(
            label='Plot',
            pos = [201,0], 
            height=400, 
            width=780
        ) as main_window: 

            dpg.add_slider_float()

            pass


        with dpg.window(
            label='Settings', 
            pos=[0,0], 
            width=200, height=400
        ) as main_window: 
            
            dpg.add_image(self.texture_tag)
            pass


    def setLearningRate(self): 
        self.update_render()

    def setSlider(self): 
        self.update_render()
  
    def update_render(self): 
        pass



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()



# I am tired man, I am going to sleep now, 
# See you later, maybe tomorrow okay.





