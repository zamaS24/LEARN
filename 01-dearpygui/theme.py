import dearpygui.dearpygui as dpg


dpg.create_context()

# set the font and the size
with dpg.font_registry():
    dpg.bind_font(
        dpg.add_font("resources/fonts/Roboto_Mono/static/RobotoMono-Regular.ttf", 22)
    )
            
with dpg.window(label="Tutorial", pos=(20, 50), width=275, height=225) as win1:
    t1 = dpg.add_input_text(default_value="some text")
    t2 = dpg.add_input_text(default_value="some text")
    with dpg.child_window(height=100):
        t3 = dpg.add_input_text(default_value="some text")
        dpg.add_input_int()
    dpg.add_input_text(default_value="some text")

with dpg.window(label="Tutorial", pos=(320, 50), width=275, height=225) as win2:
    dpg.add_input_text(default_value="some text")
    dpg.add_input_int()

with dpg.theme() as global_theme:
    """ This is just a theme you feel me bruh, """
    with dpg.theme_component(dpg.mvChildWindow ): # component
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (255, 255, 255), category=dpg.mvThemeCat_Core)
        
  

with dpg.window(tag="window_main") as main_window: 

    with dpg.group(tag="group"):
        with dpg.drawlist(width=400, height=300) as drawlist:

            # Calculate the coordinates for the white rectangle with a 1-pixel border
            x1, y1 = 0, 0  # Top-left corner, adjusted to be outside the drawing space
            x2, y2 = 399, 299  # Bottom-right corner, adjusted to cover the entire drawing space
            border_width = 1

            # Draw the white rectangle with a 1-pixel border
            dpg.draw_rectangle((x1, y1), (x2 + border_width, y2 + border_width), color=(255, 255, 255, 255), parent=drawlist)
  


dpg.bind_theme(global_theme)

dpg.show_style_editor()

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()