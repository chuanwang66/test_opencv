import numpy as np
import cv2

img = cv2.imread('image/mouse.jpg', cv2.IMREAD_COLOR)

#draw a line on img
start_pos = (0, 0)
end_pos = (50, 50)
line_color = (255, 0, 0) #BGR for opencv
line_width = 15 #in pixels
cv2.line(img, start_pos, end_pos, line_color, line_width)

#draw a rectangle on img
pos1 = (15, 25) #left top
pos2 = (200, 150) #bottom right
cv2.rectangle(img, pos1, pos2, (0, 255, 0), 5)

#draw a circle on img
center = (100, 63)
radius = 55
cv2.circle(img, center, radius, (0, 0, 255), -1) #-1 to fill in the circle

#draw a polygon on img
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
cv2.polylines(img, [pts], True, (0, 255, 255), 1) #True to connect the last point to the 1st point

#draw texts on img
font = cv2.FONT_HERSHEY_SIMPLEX
start_pos_text = (0, 130)
text_width = 1
text_thickness = 2
cv2.putText(img, 'OpenCV Sammy!', start_pos_text, font, text_width, (200, 255, 255), text_thickness, cv2.LINE_AA)

#draw image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
