import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(8,6))
a=fig.add_subplot(1,2,1,projection='3d')
b=fig.add_subplot(1,2,2,projection='3d')
x=np.arange(-3,3,0.25)
y=np.arange(-3,3,0.25)

x,y=np.meshgrid(x,y)
z=(1.8)**(-1.5*np.sqrt(x**2+y**2)*np.sin(x)*np.cos(0.5*y))
a.plot_wireframe(x,y,z)
a.set_xlabel('x')
a.set_ylabel('y')
a.set_zlabel('z')
a.set_title('meshgrid')

b.contour(x,y,z)
b.set_xlabel('x')
b.set_ylabel('y')
b.set_zlabel('z')
b.set_title('contour')
plt.show()

import numpy as np
import pandas as pd
import cv2 as cv