import cv2

prof = cv2.imread('prof.jpeg')
prof = cv2.medianBlur(prof, 5)
cv2.namedWindow('prof', cv2.WINDOW_NORMAL)
cv2.imshow('prof', prof)
cv2.waitKey(0)
cv2.destroyAllWindows()
