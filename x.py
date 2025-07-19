import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the color vertices for the cube
colors = {
    'Red': (1, 0, 0),
    'Green': (0, 1, 0),
    'Blue': (0, 0, 1),
    'Cyan': (0, 1, 1),
    'Magenta': (1, 0, 1),
    'Yellow': (1, 1, 0),
    'Black': (0, 0, 0)
}

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the cube
r = [0, 1]
X, Y = np.meshgrid(r, r)

# Create Z values as 2D arrays
Z_red = np.zeros_like(X)       # Z = 0 for Red surface
Z_green = np.ones_like(X)      # Z = 1 for Green surface
Z_blue = np.zeros_like(X)      # Z = 0 for Blue surface (left)
Z_cyan = np.ones_like(X)       # Z = 1 for Cyan surface (right)

# Define the surfaces and colors in order
ax.plot_surface(X, Y, Z_red, color=colors['Red'], alpha=0.5)        # Bottom surface (Red)
ax.plot_surface(X, Y, Z_green, color=colors['Green'], alpha=0.5)     # Top surface (Green)
ax.plot_surface(X, 0, Y, color=colors['Blue'], alpha=0.5)       # Left surface (Blue)
ax.plot_surface(X, 1, Y, color=colors['Cyan'], alpha=0.5)      # Right surface (Cyan)
ax.plot_surface(0, X, Y, color=colors['Magenta'], alpha=0.5)    # Front surface (Magenta)
ax.plot_surface(1, X, Y, color=colors['Yellow'], alpha=0.5)     # Back surface (Yellow)

# Add intersection points
intersections = {
    'Cyan': (0, 1, 1),        # Intersection of Green and Blue
    'Black': (0, 0, 0),       # Intersection of Blue and Green
    'Magenta': (1, 0, 1),     # Intersection of Red and Blue
    'Yellow': (1, 1, 0),      # Intersection of Red and Green
}

# Plot the intersection colors
for name, (x, y, z) in intersections.items():
    ax.scatter(x, y, z, color=colors[name], s=100, label=name)

# Set limits and labels
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('Red')
ax.set_ylabel('Green')
ax.set_zlabel('Blue')
ax.legend()
plt.title('3D Color Representation with Intersections')
plt.show()