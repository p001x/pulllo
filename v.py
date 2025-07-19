import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a new figure for 3D plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the cube
r = [0, 1]
X, Y = np.meshgrid(r, r)

# Create Z values as 2D arrays
Z_bottom = np.zeros_like(X)  # Bottom layer (Z = 0)
Z_top = np.ones_like(X)       # Top layer (Z = 1)

# Define colors for each corner of the cube
corner_colors = {
    (0, 0, 0): 'black',   # Black
    (1, 0, 0): 'red',     # Red
    (0, 1, 0): 'green',   # Green
    (1, 1, 0): 'yellow',   # Yellow
    (0, 0, 1): 'blue',    # Blue
    (1, 0, 1): 'magenta',  # Magenta
    (0, 1, 1): 'cyan',    # Cyan
    (1, 1, 1): 'white'    # White (top corner)
}

# Plot the edges of the cube
ax.plot_wireframe(X, Y, Z_bottom, color='k')  # Bottom edges
ax.plot_wireframe(X, Y, Z_top, color='k')     # Top edges
ax.plot_wireframe(X, 0, Y, color='k')          # Left edges
ax.plot_wireframe(X, 1, Y, color='k')          # Right edges
ax.plot_wireframe(0, X, Y, color='k')          # Front edges
ax.plot_wireframe(1, X, Y, color='k')          # Back edges

# Plot colored corners with coordinates
for (x, y, z), color in corner_colors.items():
    ax.scatter(x, y, z, color=color, s=100)  # Plot colored corners
    ax.text(x, y, z + 0.05, f'{color} ({x}, {y}, {z})', color='k', fontsize=10, ha='center')

# Define intersection points and labels
intersections = {
    'Cyan': (0, 1, 1),        # Intersection of Green and Blue
    'Black': (0, 0, 0),       # Intersection of Blue and Green
    'Magenta': (1, 0, 1),     # Intersection of Red and Blue
    'Yellow': (1, 1, 0),      # Intersection of Red and Green
}

# Plot the intersection colors and labels
for name, (x, y, z) in intersections.items():
    ax.text(x, y, z, f'{name} ({x}, {y}, {z})', color='k', fontsize=5, ha='center')

# Set limits and labels
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('Red')
ax.set_ylabel('Green')
ax.set_zlabel('Blue')
plt.title('3D Color Box with Colored Corners, Names, and Coordinates')
plt.show()