import cv2
import numpy as np
# opening
# does erosion followed by dilation
img = cv2.imread('j.png',0)
kernel = np.ones((5,5), np.uint8)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('img', img)
cv2.imshow('blackhat', blackhat)
