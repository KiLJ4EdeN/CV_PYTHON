import cv2
import numpy as np
img = cv2.imread('prof.jpeg')

# access one pixel that has 3 values for bgr
px = img[100,100]
print(px)
# accessing only blue pixel the b one.
blue = img[100,100,0]
print(blue)
img[100,100] = [255,255,255]
print(img[100,100])

# that was the slow way
# accessing RED value
img.item(10,10,2)
# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

cv2.namedWindow('window', cv2.WINDOW_NORMAL)
cv2.imshow('window', img)
