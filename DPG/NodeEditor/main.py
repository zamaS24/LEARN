import dearpygui.dearpygui as dpg

from callbacks import (
    # you can't just name thme like these, if you already don't use a class, because this just means it's not accessible outside of the calss, it's like a utility code that is 
    # repeated in the calss itself. 
    _callback_addADDNode, 
    _callback_addSUBNode, 
    _callback_delink, 
    _callback_link, 
    _callback_deleteNode
)



dpg.create_context()
dpg.set_global_font_scale(1.75)



with dpg.window(tag="main_window", label="Main Window"): 

    with dpg.menu_bar():
        with dpg.menu(label="Node"):
            # Option pour ajouter un Noeud d'addition.
            dpg.add_menu_item(
                label="Addition Node",
                callback=_callback_addADDNode
            )

            # Option pour ajouter un Noeud de soustraction.
            dpg.add_menu_item(
                label="Subtraction Node",
                callback=_callback_addSUBNode
            )


    with dpg.node_editor(
        tag="node_editor_tag",

        # callback_link : ça doit gérer tous les cas possible 
        # et garder la cohérence
        callback=_callback_link,
        delink_callback=_callback_delink
    ): # Ne pas ajouter des noeuds ici. ça doit être fait avec des callbacks
        pass


# Gérer la suppression des noeuds
with dpg.handler_registry():
    dpg.add_key_press_handler(
        key=dpg.mvKey_Delete,
        callback= _callback_deleteNode
    )
    

# Initier le viewport (Fenetre principale)
dpg.create_viewport(
    title="Node editor", width=1080,
    height=720
)

dpg.set_primary_window("main_window", True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()








with dpg.node_editor(
    'node_editor',
    user_data={'name':'hamza', 'prename':'omari'}, 
    args=None
) as node_editor: 
    

    # création d'un node editor, et mettre toutes les fonctionalités de link et delink callbacks 


    print('can you do something here or what ? ')
    print('this is not for noobs okay?')








