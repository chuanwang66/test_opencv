import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cat.png', cv2.IMREAD_GRAYSCALE)
#IMREAD_GRAYSCALE: 0
#IMREAD_COLOR: 1
#IMREAD_UNCHANGED: -1

#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')
x1, y1 = 50, 80
x2, y2 = 100, 100
plt.plot([x1, x2], [y1, y2], 'c',  linewidth=5)
plt.show()

cv2.imwrite('cat_grey.png', img)
