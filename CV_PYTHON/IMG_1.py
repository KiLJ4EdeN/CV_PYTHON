'''import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)'''
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    # the conversion
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define blue range
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # get only the blue with a thresh
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
cv2.destroyAllWindows()
