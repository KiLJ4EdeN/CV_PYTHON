import cv2
import numpy as np
img = cv2.imread('prof.jpeg', cv2.IMREAD_COLOR)
img = cv2.resize(img, (500, 500))

# perfom a filter with a kernel
# its like blurring it removes edges and averages

blur1 = cv2.blur(img, (3,3))
# well in this case they are the same

# Gaussian filter creation cv2.getGaussianKernel().
blur2 = cv2.GaussianBlur(img,(5,5),0)

median = cv2.medianBlur(img, 5)



cv2.imshow('img', img)
cv2.imshow('blur1', blur1)
cv2.imshow('blur2', blur2)
cv2.imshow('median', median)


