import cv2
import numpy as np

# preprocessing
dots = cv2.imread("polka-1.jpg")
dots2 = cv2.cvtColor(dots,cv2.COLOR_BGR2GRAY)
dots2 = cv2.blur(dots2,(3,3))

circles = cv2.HoughCircles(dots2,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=20,minRadius=1,maxRadius=40)
circles = np.uint(np.around(circles))
print(circles)

for circle in circles[0]:
    cv2.circle(dots,(circle[0],circle[1]),circle[2],(255,0,0),3)

cv2.imshow("Google",dots)
#print(circles)

cv2.waitKey(0)