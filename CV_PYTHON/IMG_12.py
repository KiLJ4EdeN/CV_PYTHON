import cv2
import numpy as np
img = cv2.imread('prof.jpeg', cv2.IMREAD_COLOR)
img = cv2.resize(img, (500, 500))


# this filter tries not to blur edges like others
# its supposed to be some sort of imporvement on gaus
# looks at neighbors but only the ones with pixel
# diffs close to this one.
# tends to not work well tho

blur = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow('img', img)
cv2.imshow('blur', blur)


