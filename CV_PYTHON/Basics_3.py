import numpy as np
import cv2
img = cv2.imread('prof.jpeg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
    print('Quitting without saving..')
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    print('Saving the gray image..')
    cv2.imwrite('profgray.jpeg',img)
    cv2.destroyAllWindows()
