# Joining images

import cv2
import numpy as np 

# Horizontal stack images

img1 = cv2.imread('resources/card.png')
img1 = cv2.resize(img1, (200,200))
img2 = cv2.imread('resources/card.jpg')
img2 = cv2.resize(img2, (200,200))

imghor = np.hstack((img1, img2))
imgvar = np.vstack((img1, img2))

cv2.imshow('stacked images horizontally', imghor)
cv2.imshow('stacked images vertically', imgvar)
cv2.waitKey(0)
 
 # Advance Stacking
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
 
img = cv2.imread('resources/card.png')
img2 = cv2.imread('resources/card.jpg')

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
imgStack = stackImages(0.5,([img,imgGray,img2],[img,img2,img]))
 

cv2.imshow("ImageStack",imgStack)
 
cv2.waitKey(0)