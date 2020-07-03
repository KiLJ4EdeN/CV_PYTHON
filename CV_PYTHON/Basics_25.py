import numpy as np
import cv2

parham = cv2.imread('parham.jpg', cv2.IMREAD_COLOR)
# width, height
# column, row
# its inveresed idiot
parham = cv2.resize(parham, (480, 640))
head = parham[150:350, 100:300]
parham[0:200, 0:200] = head
parham[0:200, 200:400] = head
parham[200:400, 100:300] = head
parham[400:600, 100:300] = head
cv2.namedWindow('parham', cv2.WINDOW_AUTOSIZE)
cv2.imshow('parham', parham)
