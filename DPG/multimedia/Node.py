import dearpygui.dearpygui as dpg
import numpy as np
from utils import black_image, white_image, convert_cv_to_dpg



class FrameNode(object):

    # to handle different tags of nodes
    id_count = 0


    # create a dpg node with an image 
    # to display the Frame data
    def __init__(
        self,
        parent, 
        frame_width, frame_height, 
        frame_data
    ):
        
        FrameNode.id_count = FrameNode.id_count +1;

        self.node_id = str(self.id_count)
        self.parent = parent
        
        # frame is dpg texture tag, the format is rgb
        # frame has: width, heihgt, tag, texture_tag 
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.texture_data = frame_data
        self.texture_tag = "texture_tag_"+self.node_id

        # register the frame since here we are handling data and not render
        with dpg.texture_registry(show=False):
            dpg.add_raw_texture(
                width = self.frame_width,
                height = self.frame_height, 
                default_value=self.texture_data, 
                tag = self.texture_tag, 
                format = dpg.mvFormat_Float_rgb
            )

        # initializing the gui node
        self._create_item_node()
         

    # creating the item and displaying the frame as black
    def _create_item_node(self):
        
        with dpg.node(
            parent=self.parent,
            tag = "node"+str(self.node_id),
            label = "node"+str(self.node_id)
        ):
            
            with dpg.node_attribute( # TODO: I guess I should add a unique tag here in a way to retrieve it later.
              attribute_type=dpg.mvNode_Attr_Static
            ):
                dpg.add_button(
                    label = "Pick image", 
                    callback = lambda : self.update_frame()
                )

            with dpg.node_attribute(
                tag="frame_att"+ self.node_id ,
                label="Frame Image",
                attribute_type=dpg.mvNode_Attr_Output
            ):
                dpg.add_image(self.texture_tag)
                   
    def update_frame(self):
        
        white_img = white_image(
            self.frame_width, 
            self.frame_height
        )

        white_texture = convert_cv_to_dpg(
            white_img, 
            self.frame_width, 
            self.frame_height
        )

        self.texture_data = white_texture

        dpg.set_value(self.texture_tag, self.texture_data)

    

class ResultNode(object):
    def __init__(self):
        pass


    def _create_item_node(self):
        pass



               





       




    
    