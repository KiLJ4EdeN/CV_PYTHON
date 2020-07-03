import cv2
import os

print(os.listdir())
parsa = cv2.imread('prof.jpeg')
parsa = cv2.resize(parsa, (400, 400))
print(parsa.shape)
cv2.imshow('parsa', parsa)
cv2.waitKey(0)
cv2.destroyAllWindows()
