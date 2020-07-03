import cv2
# addition stuff
# cv2 add goes to 255 and saturates
# numpy add tho goes further than 255 reseting to 0
# the formula for weighted add
# dst = α·img1 + β ·img2 + γ

parham = cv2.imread('parham.jpg')
logo = cv2.imread('image.png')
parham = cv2.resize(parham, (600, 400))
logo = cv2.resize(logo, (600, 400))
dst = cv2.addWeighted(parham, 0.9, logo, 0.1,0)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
