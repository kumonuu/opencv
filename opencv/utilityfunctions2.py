import cv2

# rotate image
trees = cv2.imread("trees.png")
height, width, channels = trees.shape
#matrix = cv2.getRotationMatrix2D((width/2,height/2),180,1)
#rotated_trees = cv2.warpAffine(trees,matrix,(width,height))
#cv2.imshow("Trees", rotated_trees)

# edge detection
edges = cv2.Canny(trees,100,200)
cv2.imshow("Edge detection",edges)

cv2.waitKey(0)