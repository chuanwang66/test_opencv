import cv2
import numpy as np


enable_filtering = False
enable_output = True

cap = cv2.VideoCapture(1)
#0: the 1st webcam, usually the embeded webcam
#1: the 2nd webcam, usually the plugined-in webcam

if enable_output:
	fourcc = cv2.VideoWriter_fourcc(*'XVID') #codec
	out = cv2.VideoWriter('output.avi', fourcc, 10.0, (640, 480))

#cnt = 0

while True:
	ok, frame = cap.read()

	#cnt += 1
	#if cnt == 100:
	#	cv2.imwrite('snapshot.jpg', frame)
	#	break
	cv2.imshow('title', frame)

	if enable_filtering:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('title_gray', gray)

	if cv2.waitKey(1) & 0xFF == ord('q'): #enter 'q' to break
		break

cap.release()
if enable_output:
	out.release()
cv2.destroyAllWindows()
