# Shapes and texts on images

import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
# cv2.imshow('blacked image', img)

# let's color the image

img[:] = 255,0,0
# cv2.imshow('blue image', img)

# Draw a line on the image
cv2.line(img, (0,0),(img.shape[1], img.shape[0]), (0,0,255), 2) 
cv2.rectangle(img, (0,300), (200, 400), (0,0,255), 2)
cv2.circle(img, (250, 100), 80, (0,255,0),3)
cv2.putText(img, 'OpenCV', (150, 250), cv2.FONT_HERSHEY_COMPLEX,2, (0,255,0), 2)

'''the first argument is our image, the second argument is x axis, from starting
pixel to send pixel, third argument is y axis, starting pixel and ending, and the
 last argument is the thickness of the image'''

cv2.imshow('line on image',img)
cv2.waitKey(0)