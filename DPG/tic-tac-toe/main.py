import dearpygui.dearpygui as dpg 
from tictac import TicTacToe

dpg.create_context()

# Set default font to
with dpg.font_registry():
    default_font = dpg.add_font(
        "resources/fonts/Roboto_Mono/static/RobotoMono-Regular.ttf",28)
dpg.bind_font(default_font)

TicTacToe()

dpg.show_debug()
dpg.create_viewport(
    title='Tic Tac Toe',
    width=1080,
    height=720,
    resizable=False
)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
