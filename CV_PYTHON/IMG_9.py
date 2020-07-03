import cv2
import numpy as np
img = cv2.imread('prof.jpeg', cv2.IMREAD_COLOR)
img = cv2.resize(img, (500, 500))

# perfom a filter with a kernel
# its like blurring it removes edges and averages

# kernel = np.ones((3,3),np.float32)/9
kernel = np.array([[1, 1, 1],
                   [1, 5, 1],
                   [1, 1, 1]])/13
print(kernel.shape)
print(kernel)
dst = cv2.filter2D(img,-1,kernel)
# well in this case they are the same

cv2.imshow('img', img)
cv2.imshow('dst', dst)
