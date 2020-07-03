'''
import cv2
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
'''
import cv2
import numpy as np
# mouse callback function
# if u double click a circle is drawn
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
        
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
# The namedWindow function
cv2.namedWindow('image')
# setting the call back
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
