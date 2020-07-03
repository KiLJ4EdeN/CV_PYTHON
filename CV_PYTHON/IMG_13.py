import cv2
import numpy as np

# erosion
# used for noise removal, only kernels with all one values
# result in one.

img = cv2.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img, kernel,viterations=1)

cv2.imshow('img', img)
cv2.imshow('erode', erosion)
