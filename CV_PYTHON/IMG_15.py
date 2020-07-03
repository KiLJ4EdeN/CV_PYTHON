import cv2
import numpy as np
# opening
# does erosion followed by dilation
img = cv2.imread('j.png',0)
kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# closing
# does the opp of opening
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# gradient
# diff of dilation and erosion
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# tophat
# diff of image and its opening
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow('img', img)
cv2.imshow('opening', opening)
cv2.imshow('closing', closing)
cv2.imshow('gradient', gradient)
cv2.imshow('tophat', tophat)
