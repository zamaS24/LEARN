import dearpygui.dearpygui as dpg
 

dpg.create_context()
# dpg.set_global_font_scale(1.75)

with dpg.font_registry():
            dpg.bind_font(dpg.add_font(
                "resources/fonts/Roboto_Mono/static/RobotoMono-Regular.ttf", 28))


# ----------------------------------------- Callbacks
def show_image():
    
    print("Showing the image of path C:UsersmonmsDesktopLEARNearpyguiimagejpg")
    dpg.add_image("__demo_static_texture_1", parent="image_container")

# ------------------------------------------------------------------------------------------------

dpg.add_texture_registry(label="Demo Texture Container", tag="__demo_texture_container")
dpg.add_colormap_registry(label="Demo Colormap Registry", tag="__demo_colormap_registry")



## create static textures
texture_data1 = []
for i in range(100*100):
    texture_data1.append(255/255)
    texture_data1.append(0)
    texture_data1.append(255/255)
    texture_data1.append(255/255)

dpg.add_static_texture(width=100, height=100, default_value=texture_data1, parent="__demo_texture_container", tag="__demo_static_texture_1", label="Static Texture 1")
    

with dpg.window(label="Tutorial", width=800, height=300):
    dpg.add_button(label="Show Image", callback=show_image)
    with dpg.group(tag="image_container"):
        dpg.add_text("Image")
        



dpg.create_viewport(title='Images and textures', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()