import cv2

img = cv2.imread("image.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
print(img)
cv2.imshow("Image",img)

cv2.waitKey(0)