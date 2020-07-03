import cv2
# addition stuff
# cv2 add goes to 255 and saturates
# numpy add tho goes further than 255 reseting to 0
# the formula for weighted add
# dst = α·img1 + β ·img2 + γ

parham = cv2.imread('parham.jpg')
logo = cv2.imread('logo.png')
parham = cv2.resize(parham, (600, 400))
logo = cv2.resize(logo, (600, 400))
print(parham.shape, logo.shape)
numpy_add = parham + logo
cv_add = cv2.add(parham, logo)
cv2.imshow('np_add', numpy_add)
cv2.imshow('cv_add', cv_add)

