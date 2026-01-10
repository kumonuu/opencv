import cv2
import numpy as np

trees = cv2.imread("trees.png")

# shapes
cv2.line(trees,(100,100),(200,200),(255,0,0),5)
cv2.rectangle(trees,(300,100),(400,200),(0,255,0),-1)
cv2.circle(trees,(500,100),64,(0,0,255),-1)

# add text
cv2.putText(trees,'JetLearn',(100,400),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),3,cv2.LINE_8)
cv2.putText(trees,'JetLearn',(100,500),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),3,cv2.LINE_4)

# polygon
pts = [[10,5],[20,30],[70,20]]
pts = np.array(pts).reshape(-1,1,2)
cv2.polylines(trees,[pts],True,(255,0,255))

print(pts.shape)
print(pts)

cv2.imshow("Trees",trees)

cv2.waitKey(0)