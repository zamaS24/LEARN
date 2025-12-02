import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

# Generate some 3D coordinates
x = np.random.rand(10)
y = np.random.rand(10)
z = np.random.rand(10)

# Create a 3D plot
fig = plt.figure()
ax = plt.axes(projection="3d")

# Plot the 3D coordinates
ax.scatter3D(x, y, z, c=z, cmap='viridis')

# Add labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Scatter Plot')

# Show the plot
plt.show()