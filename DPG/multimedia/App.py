import dearpygui.dearpygui as dpg

from utils import debug
from callbacks import _callback_delink, _callback_link, callback_add_frame_node





class App: 
    
    """
        The `node editor` item and it's callbacks.
        
        TODO: shall I split the nodes to separate classes? 
            maybe it would be more cleaner. 
    """

    def __init__(self): 
        

        self._set_font(
            path="resources/fonts/Roboto_Mono/static/RobotoMono-Regular.ttf",
            font_size=28
        )
               
        with dpg.window(
            tag="tag_main_window", 
            width=1080, height=720,       
        ):
            # Menu : adding nodes, selecting algorithm
            with dpg.menu_bar():
                    
                dpg.add_menu_item(
                    tag="",
                    label="Frame Node   ", 
                    callback=callback_add_frame_node)
                
                with dpg.menu(label="Select algorithm   "):
                    dpg.add_menu_item(
                        label="Linear Search",
                        tag="tag_menu_linear", 
                        callback=debug 
                    )
                    dpg.add_menu_item(
                        label="logarithm search",
                        tag="tag_menu_logarithm", 
                        check=True,
                        callback=debug 
                    )

           
            # The node editor space
            with dpg.node_editor(
                tag="tag_node_editor", 
                callback =_callback_link,
                delink_callback=_callback_delink,
                minimap=True,
                minimap_location=dpg.mvNodeMiniMap_Location_BottomRight
            ):
                pass
                
        
        
        self._set_main_window()
        

    
    def _set_main_window(self):
        dpg.set_primary_window("tag_main_window", True)

    def _set_font(self, path, font_size): 
        with dpg.font_registry():
            default_font = dpg.add_font(
                path,
                font_size
            )
        dpg.bind_font(default_font)




