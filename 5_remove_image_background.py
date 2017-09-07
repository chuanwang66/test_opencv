#-*- coding:utf-8 -*-
'''
	越有东西的地方，越黑，即越接近0
'''
import cv2
import numpy as np

ceiling = cv2.imread('image/ceiling.jpg')
mouse = cv2.imread('image/mouse.jpg')

mouse_gray = cv2.cvtColor(mouse, cv2.COLOR_BGR2GRAY)

#ok, mask_inv = cv2.threshold(mouse_gray, 100, 255, cv2.THRESH_BINARY_INV)
#mask = cv2.bitwise_not(mask_inv)
ok, mask = cv2.threshold(mouse_gray, 90, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

#dst = cv2.bitwise_and(src1, src2, mask): dst = src1 & src2 & mask
ceiling_bg = cv2.bitwise_and(ceiling, ceiling, mask=mask) #dig the 'mask' out of ceiling
mouse_fg = cv2.bitwise_and(mouse, mouse, mask=mask_inv)

dst = cv2.add(ceiling_bg, mouse_fg)

#cv2.imshow('mask_inv', mask_inv)
#cv2.imshow('ceiling_bg', ceiling_bg)
#cv2.imshow('mouse_fg', mouse_fg)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()