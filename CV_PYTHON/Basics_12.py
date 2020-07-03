import numpy as np
import cv2
# Create a black image
# np.zeros (size, type)
# img = np.zeros((256, 256, 3), np.uint16)
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# center , big, small axes
# 360 for full elipse
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
