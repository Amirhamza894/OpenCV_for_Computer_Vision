# Resizing and croping

import cv2
import numpy as np 

img = cv2.imread('resources/girl.jpg')
print(img.shape)
imgresize = cv2.resize(img, (400, 533))
print(imgresize.shape)
imgcrop = img[30:470, 80:480]
cv2.imshow('girl resize image',imgresize)
cv2.imshow('girl image', img)
cv2.imshow('croped', imgcrop)
cv2.waitKey(0)