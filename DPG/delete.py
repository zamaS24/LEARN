import dearpygui.dearpygui as dpg 



dpg.create_context()


with dpg.window(tag="tag_window_main"): 
    dpg.add_text(default_value="Some text here...")


dpg.create_viewport(title="TizTiz")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


if dpg.is_dearpygui_running:
    print(f"Dearpygui is not running!\n")