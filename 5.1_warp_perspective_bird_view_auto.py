import cv2
import numpy as np 

list_value = np.zeros((4,2), int)
print(list_value)
value = 0
def click(event, x,y, flags, param):
    global value
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y),5, (255,0,0), -1)
        list_value[value] = x,y
        value = value + 1
        print(x,y)


img = cv2.imread('resources/card.jpg')

print(img.shape)

height = img.shape[0]
width = img.shape[1]

while True:
    if value == 4:
        point = np.float32([list_value[0], list_value[1], list_value[2], list_value[2]])
        point2 = np.float32([[0,0], [width,0], [0,height], [width,height]])
        matrix = cv2.getPerspectiveTransform(point, point2)
        final = cv2.warpPerspective(img, matrix, (width,height))
        cv2.imshow('output', final)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', click)
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

