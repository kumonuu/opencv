import cv2, numpy as np

shapes = cv2.imread("shapes.jpg")

# preprocessing
shapes_gs = cv2.cvtColor(shapes,cv2.COLOR_BGR2GRAY)

# corner detection
corners = cv2.goodFeaturesToTrack(shapes_gs,27,0.01,10,useHarrisDetector=False)
corners = np.intp(corners)

for corner in corners:
    corner = corner.ravel()
    cv2.circle(shapes,(corner[0],corner[1]),5,(255,0,0),-1)

cv2.imshow("Corner Detection",shapes)

cv2.waitKey(0)