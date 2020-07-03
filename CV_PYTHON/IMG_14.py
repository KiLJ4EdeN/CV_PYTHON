import cv2
import numpy as np

# dilation opp of erosion
# used after noise removal,  kernels with only one value of 1
# result in one.

img = cv2.imread('j.png',0)
kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('img', img)
cv2.imshow('dilation', dilation)
