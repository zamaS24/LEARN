"""A simple interface for dearpygui"""

import dearpygui.dearpygui as dpg


dpg.create_context()
dpg.set_global_font_scale(1.75)
dpg.create_viewport(title="Main App")


def print_me(sender):
    """Just a test function"""

    print('Sender: ', sender)



def endless_task(sender, app_data, user_data):
    "endless task to test responsivness and non blocking of stuff"
    x = 0
    while True:
        x += 1
        if x%100000 == 0: 
            print(x)

    return x


with dpg.viewport_menu_bar():
    with dpg.menu(label="File"):
        dpg.add_menu_item(label="Save", callback=print_me)
        dpg.add_menu_item(label="Save As", callback=print_me)



        with dpg.menu(label="Settings"):
            dpg.add_menu_item(label="Setting 1", callback=print_me, check=True)
            dpg.add_menu_item(label="Setting 2", callback=print_me)

    dpg.add_menu_item(label="Help", callback=print_me)


               
    with dpg.menu(label="Widget Items"):
        dpg.add_checkbox(label="Pick Me", callback=print_me)
        dpg.add_button(label="Press Me", callback=print_me)
        dpg.add_color_picker(label="Color Me", callback=print_me)
        dpg.add_file_dialog(label="file dialog")
        dpg.add_button(label="endless task", callback=endless_task)


    with dpg.window(): 
            with dpg.child_window(label='child window'): 
                dpg.add_button(label='submit')
           




dpg.setup_dearpygui()
dpg.show_viewport()

dpg.start_dearpygui() # this is the event loop right?
dpg.destroy_context()


