import cv2
import numpy as np
img = cv2.imread('prof.jpeg')
res = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
#OR
height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

cv2.imshow('prof', img)
cv2.imshow('resized', res)

print([i for flag in dir(cv2) if i.startswith('INTER_')])
