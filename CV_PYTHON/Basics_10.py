import numpy as np
import cv2
# Create a black image
# np.zeros (size, type)
# img = np.zeros((256, 256, 3), np.uint16)
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.rectangle(img, (100,100), (400,400),(255,0,0), -1)
img = cv2.circle(img, (250,250), 150, (0,0,255), -1)
img = cv2.line(img, (100,100), (400,400),(0,255,0), 16)
img = cv2.line(img, (100,400), (400,100), (0,255,0), 16)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
