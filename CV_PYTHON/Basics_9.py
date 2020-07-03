import numpy as np
import cv2
# Create a black image
# np.zeros (size, type)
# img = np.zeros((256, 256, 3), np.uint16)
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(512,512),(255,0,0),42)
img = cv2.line(img, (0,512), (512, 0), (255,0,0),42)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
