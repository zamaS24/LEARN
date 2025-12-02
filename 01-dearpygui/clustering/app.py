import dearpygui.dearpygui as dpg 


def _hsv_to_rgb(h, s, v):
    if s == 0.0: return (v, v, v)
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i; p,q,t = v*(1.-s), v*(1.-s*f), v*(1.-s*(1.-f)); i%=6
    if i == 0: return (255*v, 255*t, 255*p)
    if i == 1: return (255*q, 255*v, 255*p)
    if i == 2: return (255*p, 255*v, 255*t)
    if i == 3: return (255*p, 255*q, 255*v)
    if i == 4: return (255*t, 255*p, 255*v)
    if i == 5: return (255*v, 255*p, 255*q)


def clbk_exe_clustering(sender, app_data, user_data):
    print(f"I was fired from {sender}, and app data = {app_data}, and user data = {user_data}")


class App: 
    
    def __init__(self): 

        # For the theme
        with dpg.theme(tag="__demo_theme"+str(1)):
                            with dpg.theme_component(dpg.mvButton):
                                dpg.add_theme_color(dpg.mvThemeCol_Button, _hsv_to_rgb(5/7.0, 0.6, 0.6))
                                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, _hsv_to_rgb(5/7.0, 0.8, 0.8))
                                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, _hsv_to_rgb(5/7.0, 0.7, 0.7))
                                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 1*5)
                                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 1*3, 1*3)

        # Fenetre principale
        with dpg.window(tag="wdw_main", label= "Clustering", height = 720, width = 1080):
   
            # Text Display
            dpg.add_text("" ,tag="txt_description")

            # Button to execute clustering 
            dpg.add_button(tag="btn_file", label = "Executer clustering", callback=clbk_exe_clustering, user_data="just some text")

        
        
dpg.create_context()
App()
dpg.create_viewport(title='Projet FD, Clustering', width=1080, height=720, resizable=False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()