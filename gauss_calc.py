import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import os
from PIL import Image
import laserbeamsize as lbs

import cv2
name = r"C:\Users\Gaetan\Desktop\image.jpg"
im_gray = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
plt.imshow(im_gray)
plt.show()
x, y, dx, dy, phi = lbs.beam_size(im_gray)
size = 4.65

print("The center of the beam ellipse is at (%.0f, %.0f)" % (x, y))
print(f"The ellipse diameter (closest to horizontal) is {dx*size} micron")
print(f"The ellipse diameter (closest to   vertical) is {dy*size}micron")
print("The ellipse is rotated %.0f° ccw from the horizontal" %
      (phi*180/3.1416))
plt.figure(2)
lbs.beam_size_and_plot(im_gray, pixel_size=size)
plt.show()
