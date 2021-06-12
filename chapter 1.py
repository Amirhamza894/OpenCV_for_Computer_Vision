### Import an image

import cv2
print('Package imported')

img = cv2.imread("C:/Users/hp/Desktop/opencv/resources/cattura-1.jpg")

cv2.imshow('output image', img)

cv2.waitKey(0)

### Import a video

vid = cv2.VideoCapture('C:/Users/hp/Desktop/opencv/resources/videoplayback.mp4')

while True:
    source, img = vid.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        # This will play video fast

# Read webcam

vid = cv2.VideoCapture(0)
vid.set(3, 640) # height
vid.set(4, 480)# weight
vid.set(10,100) # brightness
while True:
    source, img = vid.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break