import dearpygui.dearpygui as dpg

def _callback_link(sender, app_data, user_data):
    global linked_items;
    pass

def _callback_delink(sender, app_data, user_data):
    pass

def _callback_deleteNode():
    def debug():
        print("****** Debugging delete Node ******")
        print("dpg.get_selected_nodes :", dpg.get_selected_nodes("node_editor_tag"))
        print()

    debug()
    dpg.delete_item(
        dpg.get_selected_nodes("node_editor_tag")
    )
    pass

def _callback_addADDNode(sender, app_data, user_data):

    def info():
        print("****** Infos ADDNODE ******")
        print("sender :" + str(sender))
        print("app_data : " + str(app_data))
        print("user_data : " + str(user_data))
        print()
    info()

    # Creer un noeud d'addition avec deux `slider float`
    with dpg.node(label="Node 1", parent="node_editor_tag"):
            
            # first attribute 
            with dpg.node_attribute(
                label="Node A1", 
                attribute_type=dpg.mvNode_Attr_Input
            ):
                dpg.add_input_float(label="F1", width=150)

            # second attribute
            with dpg.node_attribute(
                label="Node A2",
                attribute_type=dpg.mvNode_Attr_Input
            ):
                dpg.add_input_float(label="F2", width=150)
            
    pass

def _callback_addSUBNode():
    pass




def cbk_link_node(sender, app_data, user_data): 

    # get the source node & the input type 
    item_id = sender

    # get the destination node & the input type 




    pass 



# okay so maybe it's time do make linux and download stuff right man?
# Well I hope so lol thank you so much for this one too mate okay