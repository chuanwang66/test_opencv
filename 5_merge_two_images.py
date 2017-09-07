import cv2
import numpy as np

img1 = cv2.imread('image/mouse.jpg')
img2 = cv2.imread('image/ceiling.jpg')

#add = img1 + img2
#add = cv2.add(img1, img2) #pretty white for R1+R2 may be over 255, which goes the same for B&G
#add = cv2.add(img1//2, img2//2)

add = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

cv2.imshow('add', add)
cv2.waitKey(0)
cv2.destroyAllWindows()