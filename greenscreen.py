import cv2, numpy as np

field = cv2.imread("field.jpg")
spongebob = cv2.imread("spongebob.jpg")
height, width, channels = field.shape
spongebob = cv2.resize(spongebob,(width,height))
spongebob2 = cv2.cvtColor(spongebob,cv2.COLOR_BGR2HSV)

lower_green = np.array([45,50,50])
upper_green = np.array([79,255,255])
sb_mask = cv2.inRange(spongebob2,lower_green,upper_green)
field_mask = cv2.bitwise_not(sb_mask)

field2 = cv2.bitwise_and(field,field,mask=sb_mask)
spongebob3 = cv2.bitwise_and(spongebob,spongebob,mask=field_mask)
weighted_sum = cv2.addWeighted(field2,1.0,spongebob3,1.0,0)

cv2.imshow("Spongebob", weighted_sum)

cv2.waitKey(0)