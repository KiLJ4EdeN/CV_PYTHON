import numpy as np
import cv2
# Create a black image
# np.zeros (size, type)
# img = np.zeros((256, 256, 3), np.uint16)
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# center , big, small axes
# 360 for full elipse
img = cv2.ellipse(img,(256,256),(100,50),0,0,360,255,-1)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
