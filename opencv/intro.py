import cv2

img = cv2.imread("image.png",0)
cv2.imshow("Image",img)
print(img)

cv2.waitKey(0)