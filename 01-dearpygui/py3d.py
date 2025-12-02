import open3d as o3d
import dearpygui.dearpygui as dpg
import dearpygui.dearpygui as dpg
import open3d as o3d

dpg.create_context()
# Define a callback function to create the point cloud
def create_point_cloud():
    # Load a point cloud from a file
    pcd = o3d.io.read_point_cloud("p213.pcd")

    # Create a visualization window
    vis = o3d.visualization.Visualizer()

    # Add the point cloud to the visualization
    vis.create_window()
    vis.add_geometry(pcd)

    # Run the visualization
    vis.run()

# Create the GUI
with dpg.window():
    dpg.add_text("My Point Cloud Viewer")
    dpg.add_button(label="Load Point Cloud", callback=create_point_cloud)


dpg.create_viewport(title='ZAKAMO', width=1080, height=720, resizable=False)

dpg.setup_dearpygui()
dpg.show_viewport()

dpg.start_dearpygui()
dpg.destroy_context()