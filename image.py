import numpy as np
import pandas as pd
import cv2 as cv
from google.colab.patches import cv2_imshow
from skimage import io
from PIL import Image
import matplotlib.pyplot as plt

url='https://i5.walmartimages.com/asr/7621463c-60e1-4846-bd32-09c47a13ba9e.9141767d784a3eb5e4814a0e0d414822.jpeg'
myimg=io.imread(url)
gray_image=cv.cvtcolor(myimg,cv.COLOR_BGR2GRAY)
img_mat=np.array(list(gray_image),float)
print(img_mat)
img_mat.shape
plt.imshow(img_mat)
img_mat.shape