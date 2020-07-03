import cv2
import numpy as np

img = cv2.imread('prof.jpeg', -1)
# cv2.WINDOW_AUTOSIZE is default
# but with this we can resize the window.
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
