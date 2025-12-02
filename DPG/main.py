import dearpygui.dearpygui as dpg
from tutorials import Test, Handler, Board, DpgCv
import cv2 as cv
import numpy as np


from typing import Any

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
 
# The idea of Node attributes is that, 
# I shall manage the Tags of the elements

def link_callback(sender, app_data):
    # app_data -> (link_id1, link_id2)
    # app_data[0] and app_data[1] are when user attempts to link 

    def debug():
        print(f"**[DEBUG] link callback  **")
        print(f"sender     \t:  {sender}")
        print(f"app_data[0]\t:  {app_data[0]}")
        print(f"app_data[1]\t:  {app_data[1]}")
        print()

    debug()
    # create the link between the two 
    dpg.add_node_link(
        app_data[0], 
        app_data[1], 
        tag="N1A1_N2A2",
        parent=sender)
    
    

# callback runs when user attempts to disconnect attributes
def delink_callback(sender:Any, app_data:Any) -> None: 
    # app_data -> link_id
    
    def show_info():
        print(f"** delink callback information **")
        print(f"sender      :  {sender}")
        print(f"app_data    :  {app_data}")
        print()

    show_info()
    dpg.delete_item(app_data)
   



with dpg.window(label="Tutorial", width=1200, height=800, pos=[0,0]):

    # Node editor: the big area where you can place your Nodes.
    with dpg.node_editor(
        tag = "tag_node_editor",
        callback=link_callback, 
        delink_callback=delink_callback
    ):
        # Type 1 node
        with dpg.node(tag="tag_node_1", label="Node 1"):

            # First dot of connection
            with dpg.node_attribute(
                tag="tag_node_1_att_1",
                label="Node A1", 
                attribute_type= dpg.mvNode_Attr_Output
            ):
                dpg.add_input_float(label="F1", width=150)
                dpg.add_button(label="Execute")
                
        
        # Type 2 node
        with dpg.node(tag="tag_node_2", label="Node 2"):

            with dpg.node_attribute(
                tag="tag_node_2_att_2",
                label="Node A2"):
                dpg.add_input_float(label="F3", width=200)


show_debugtools()
dpg.create_viewport(title="Something here ")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()




if dpg.is_dearpygui_running:
    print(f"Dearpygui is not running!\n")





class NodeEditor(object): 

    __nodeid = 0
    __nodeList = []
    __node_tag_template = 'tag_node_{id}'
    __node_editor_tag_template = 'tag_node_editor_{id}'



    def __init__(self):
        self

    def __getitem__(self, index:int) -> dpg.node: 
        pass




    with dpg.node_editor(): 
        pass 

    # process node to make it happen right ?




class DPG_NODE_ABC(object): 

    def __init__(self) -> None: 
        pass 


    @abs
    def something(self, idx:int) -> None: 
        pass 


class ListeningToAllThoseStuff(object): 

    def __init__(self, *args, **kargs)-> None: 
        pass 


    def __getitem__(self, idx:int) -> None: 
        pass 


    def __call__(self, *args, **kargs) -> None: 
        pass 

    def __do_some(self, *args, **kargs) -> None:
        pass 

    @staticmethod
    def count_elmenets(*args) -> None: 
        pass 



    # you also know how to do with JS right ? 




    """CSS: 

    divs: inline and 

    CSS BOX model:
        -> padding 
        ->content 
        -> border
        -> outlier
        ->margin
    
        
    CSS Design: 
        -> flex box : align items, flex-direction:
        -> grid: 
        -> display: block , inline, inline-block


        -> positioning : how to make a navBar.
        -> 
        -> 

    """




