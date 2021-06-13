# WARP PRESPECTIVE

import cv2
import numpy as np

img = cv2.imread('resources/card.jpg')
print(img.shape)

height = img.shape[0]
width = img.shape[1]
pts1 = np.float32([[169, 30], [278, 81], [95, 194], [202, 246]])

pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
final = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('image', img)
cv2.imshow('output image', final)
cv2.waitKey(0)





# print(height)
# print(weight)