## OpenCV Basic Functions

import cv2
import numpy as np 

img = cv2.imread('resources/girl.jpg')
kernel = np.ones((4,4), np.uint8)
# Converting into GrayScale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur Image
blurimg = cv2.GaussianBlur(imgGray, (7,7), 0)
# Canny Image
Cannyimg = cv2.Canny(img, 150,100)
# image dilation
imgdilation = cv2.dilate(Cannyimg, kernel, iterations = 1)
# Eroded image
imgeroded = cv2.erode(imgdilation, kernel, iterations=1)

# cv2.imshow('Gray Image',imgGray)
# cv2.imshow('blur Image', blurimg)
cv2.imshow('Canny Image', Cannyimg)
cv2.imshow('dilate image', imgdilation)
cv2.imshow('eroded image', imgeroded)
cv2.waitKey(0)