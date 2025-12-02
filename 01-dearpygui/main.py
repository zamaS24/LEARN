import dearpygui.dearpygui as dpg
import cv2 as cv
import math
import numpy as np 

dpg.create_context()

global Association_window 

textArea = None
dpg.set_global_font_scale(1.75)
dpg.bind_font("NotoSerifCJKjp-Medium.otf")
size = 5
verticies = [
        [-size, -size, -size],  # 0 near side
        [ size, -size, -size],  # 1
        [-size,  size, -size],  # 2
        [ size,  size, -size],  # 3
        [-size, -size,  size],  # 4 far side
        [ size, -size,  size],  # 5
        [-size,  size,  size],  # 6
        [ size,  size,  size],  # 7
        [-size, -size, -size],  # 8 left side
        [-size,  size, -size],  # 9
        [-size, -size,  size],  # 10
        [-size,  size,  size],  # 11
        [ size, -size, -size],  # 12 right side
        [ size,  size, -size],  # 13
        [ size, -size,  size],  # 14
        [ size,  size,  size],  # 15
        [-size, -size, -size],  # 16 bottom side
        [ size, -size, -size],  # 17
        [-size, -size,  size],  # 18
        [ size, -size,  size],  # 19
        [-size,  size, -size],  # 20 top side
        [ size,  size, -size],  # 21
        [-size,  size,  size],  # 22
        [ size,  size,  size],  # 23
    ]

colors = [
        [255,   0,   0, 150],
        [255, 255,   0, 150],
        [255, 255, 255, 150],
        [255,   0, 255, 150],
        [  0, 255,   0, 150],
        [  0, 255, 255, 150],
        [  0,   0, 255, 150],
        [  0, 125,   0, 150],
        [128,   0,   0, 150],
        [128,  70,   0, 150],
        [128, 255, 255, 150],
        [128,   0, 128, 150]
    ]

width, height, channels, data = dpg.load_image('imageL.jpg') # 0: width, 1: height, 2: channels, 3: data

with dpg.texture_registry():
    dpg.add_static_texture(width, height, data, tag="image_id")

def add_text(sender, data): 
    global textArea
    print(f"Sender:{sender}, data:{data}")
    paragraph1 = "Thank you \n"
    textArea = dpg.add_text(paragraph1, wrap=0, parent="secondary_window")

def close(): 
    # dpg.hide_item("Wdw_main")
    pass

def function():
    value = dpg.get_value("slider")
    print(f"slider value is :{value}")
    dpg.configure_item("secondary_window", show=True)
    pass

def delete(sender, data, userdata):
    print(f"sender:{sender}, data:{data}, userdata:{userdata}")
    # dpg.delete_item("secondary_window", children_only=True)
    dpg.delete_item(textArea)

def file_dialog_callback(sender, data):
    file_path = dpg.get_value("File Dialog##dialog")
    if file_path is None:
        print("No file selected.")
    else:
        print("Selected file:", file_path)

def toggle_layer2(sender):
    show_value = dpg.get_value(sender)
    dpg.configure_item("layer2", show=show_value)








#________ ACTUAL GUI


with dpg.window(tag='Wdw_main', label="Main Window", no_resize=True, no_close=True,no_open_over_existing_popup=True, width=300, height=250 ):
    dpg.add_text('Apriori et Close \nTP FD\nBy Hamza/Hamzaoui')
    dpg.add_button(tag='Fichier', label="Choisir un fichier")
    # dpg.add_input_text(tag = 'pInpuText',label='string', default_value="Quick brown fox")
    dpg.add_slider_float(tag = 'slider',label="Minsup", default_value=0.273, max_value=1)

    dpg.add_spacer(height=10)
    btnApriori = dpg.add_button(tag='btn_apriori',label='Apriori',callback=function)
    dpg.add_same_line()
    btnClose = dpg.add_button(tag='btn_close', label='Close', callback=close)

with dpg.window(label="Apriori, Association rules", tag="secondary_window", show= False, no_resize=True, no_close=True,
                 no_open_over_existing_popup=True, pos=(310,0) ,width=300, height=250 ) as Association_window:
    dpg.add_button(label="AddText", callback=add_text)
    
    # How could


with dpg.window(tag="anothe_window", label="anotherwindow"):
    dpg.add_button(label="Delete Text", callback=delete)
    pass

# with dpg.window(label="Tutorial2"):
#     dpg.add_checkbox(label="Radio Button1", tag="R1")
#     dpg.add_checkbox(label="Radio Button2", source="R1")

#     dpg.add_input_text(label="Text Input 1")
#     dpg.add_input_text(label="Text Input 2", source=dpg.last_item(), password=True)


# with dpg.window(label="Main"):

#     with dpg.menu_bar():
#         with dpg.menu(label="Themes"):
#             dpg.add_menu_item(label="Dark")
#             dpg.add_menu_item(label="Light")
#             dpg.add_menu_item(label="Classic")

#             with dpg.menu(label="Other Themes"):
#                 dpg.add_menu_item(label="Purple")
#                 dpg.add_menu_item(label="Gold")
#                 dpg.add_menu_item(label="Red")

#         with dpg.menu(label="Tools"):
#             dpg.add_menu_item(label="Show Logger")
#             dpg.add_menu_item(label="Show About")

#         with dpg.menu(label="Oddities"):
#             dpg.add_button(label="A Button")
#             dpg.add_simple_plot(label="Menu plot", default_value=(0.3, 0.9, 2.5, 8.9), height=80)


#Drawing API
with dpg.window(label="Tutorial"):
    dpg.add_checkbox(label="show layer", callback=toggle_layer2, default_value=True)
    with dpg.drawlist(width=width, height=height):  # or you could use dpg.add_drawlist and set parents manually
        # dpg.draw_line((10, 10), (100, 100), color=(255, 0, 0, 255), thickness=1)
        # dpg.draw_text((0, 0), "Origin", color=(250, 250, 250, 255), size=15)
        # # dpg.draw_arrow((50, 70), (100, 65), color=(0, 200, 255), thickness=5, size=10)
        # dpg.draw_circle(center=(50, 70), radius=50, color=(0, 200, 255),fill=(255, 255, 255, 255), show=True, thickness=5)

        # dpg.draw_image("image_id", (0, 400), (200, 600), uv_min=(0, 0), uv_max=(1, 1))
        # dpg.draw_image("image_id", (400, 300), (600, 500), uv_min=(0, 0), uv_max=(0.5, 0.5))
        dpg.draw_image("image_id", (0, 0), (width, height), uv_min=(0, 0), uv_max=(1, 1))

        with dpg.draw_layer():
            dpg.draw_line((10, 10), (100, 100), color=(255, 0, 0, 255), thickness=1)
            dpg.draw_text((0, 0), "Origin", color=(250, 250, 250, 255), size=15)
            dpg.draw_arrow((50, 70), (100, 65), color=(0, 200, 255), thickness=1, size=10)

        with dpg.draw_layer(tag="layer2"):
            dpg.draw_line((10, 60), (100, 160), color=(255, 0, 0, 255), thickness=1)
            dpg.draw_arrow((50, 120), (100, 115), color=(0, 200, 255), thickness=1, size=10)
    
    with dpg.drawlist(width=500, height=500, show=False):

        with dpg.draw_layer(tag="main pass", depth_clipping=True, perspective_divide=True, cull_mode=dpg.mvCullMode_Back):

            with dpg.draw_node(tag="cube"):

                dpg.draw_triangle(verticies[1],  verticies[2],  verticies[0], color=[0,0,0.0],  fill=colors[0])
                dpg.draw_triangle(verticies[1],  verticies[3],  verticies[2], color=[0,0,0.0],  fill=colors[1])
                dpg.draw_triangle(verticies[7],  verticies[5],  verticies[4], color=[0,0,0.0],  fill=colors[2])
                dpg.draw_triangle(verticies[6],  verticies[7],  verticies[4], color=[0,0,0.0],  fill=colors[3])
                dpg.draw_triangle(verticies[9],  verticies[10], verticies[8], color=[0,0,0.0],  fill=colors[4])
                dpg.draw_triangle(verticies[9],  verticies[11], verticies[10], color=[0,0,0.0], fill=colors[5])
                dpg.draw_triangle(verticies[15], verticies[13], verticies[12], color=[0,0,0.0], fill=colors[6])
                dpg.draw_triangle(verticies[14], verticies[15], verticies[12], color=[0,0,0.0], fill=colors[7])
                dpg.draw_triangle(verticies[18], verticies[17], verticies[16], color=[0,0,0.0], fill=colors[8])
                dpg.draw_triangle(verticies[19], verticies[17], verticies[18], color=[0,0,0.0], fill=colors[9])
                dpg.draw_triangle(verticies[21], verticies[23], verticies[20], color=[0,0,0.0], fill=colors[10])
                dpg.draw_triangle(verticies[23], verticies[22], verticies[20], color=[0,0,0.0], fill=colors[11])
        




    
x_rot = 10
y_rot = 45
z_rot = 0

view = dpg.create_fps_matrix([0, 0, 50], 0.0, 0.0)

proj = dpg.create_perspective_matrix(math.pi*45.0/180.0, 1.0, 0.1, 100)

model = dpg.create_rotation_matrix(math.pi*x_rot/180.0 , [1, 0, 0])*\
                        dpg.create_rotation_matrix(math.pi*y_rot/180.0 , [0, 1, 0])*\
                        dpg.create_rotation_matrix(math.pi*z_rot/180.0 , [0, 0, 1])





dpg.set_clip_space("main pass", 0, 0, 500, 500, -1.0, 1.0)
dpg.apply_transform("cube", proj*view*model)

# dpg.set_primary_window("wdw_parameters", True)
dpg.create_viewport(title='ZAKAMO', width=1080, height=720, resizable=False)
# dpg.create_viewport(title="anotherone" )
dpg.setup_dearpygui()
dpg.show_viewport()

dpg.start_dearpygui()
dpg.destroy_context()


