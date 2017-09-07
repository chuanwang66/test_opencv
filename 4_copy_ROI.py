import numpy as np
import cv2

img = cv2.imread('image/mouse.jpg', cv2.IMREAD_COLOR)

img[55, 55] = [255, 255, 255] #set the pixel to white
px = img[55, 55]
print(px)

row1, col1 = 183, 89  #left-top
row2, col2 = 395, 425 #right-bottom
rows, cols = row2 - row1, col2 - col1
mouse = img[row1:row2, col1:col2] #ROI(Region of Image)
img[0:rows, 0:cols] = mouse #copy ROI


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()