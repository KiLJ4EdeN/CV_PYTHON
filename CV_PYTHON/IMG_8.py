import cv2
import numpy as np
img = cv2.imread('prof.jpeg', cv2.IMREAD_COLOR)
img = cv2.resize(img, (500, 500))

# perfom a filter with a kernel

kernel = np.ones((3,3),np.float32)/9
dst = cv2.filter2D(img,-1,kernel)
cv2.imshow('img', img)
cv2.imshow('dst', dst)


