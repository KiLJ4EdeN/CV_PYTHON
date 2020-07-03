import cv2
import numpy as np
img = cv2.imread('prof.jpeg')

print(img.shape)
print(img.size)
print(img.dtype)
# splitting the colors
b, g, r = cv2.split(img)
# merge back
img = cv2.merge((b, g, r))
# remove some color like red
# img[:, :, 2] = 0
# rgb to bgr
img = img[:, :, ::-1]
cv2.namedWindow('window', cv2.WINDOW_NORMAL)
cv2.imshow('window', img)
