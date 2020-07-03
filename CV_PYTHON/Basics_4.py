import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('prof.jpeg',0)
# opencv loads in bgr and mayplotlib needs rgb
# might cause errors if you forget to make the conversion
# with cv2.cvtColor
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
# to hide tick values on X and Y axis
plt.show()
