import cv2
import numpy as np

print(cv2.__version__)
# 0 means gray, 1 and -1 are for color and untouched(alpha channel)
# respectively.
parsa = cv2.imread('prof.jpeg', -1)
parsa = cv2.resize(parsa, (400, 400))
print(parsa.shape)
cv2.imshow('parsa', parsa)
cv2.waitKey(0)
cv2.destroyAllWindows()
