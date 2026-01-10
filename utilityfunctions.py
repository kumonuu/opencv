import cv2

trees = cv2.imread("trees.png")
quote = cv2.imread("quote.png")

# adding and subtracting images
height, width, channels = trees.shape
quote = cv2.resize(quote, (width, height))
#combined = cv2.addWeighted(trees,0.9,quote,0.5,0)
#subtracted_img = cv2.subtract(quote,trees)

#cv2.imshow("Combined Image",subtracted_img)

#blurring
#trees = cv2.blur(trees,(7,7))
#trees = cv2.GaussianBlur(trees,(7,7),0)
#trees = cv2.medianBlur(trees,7)
#cv2.imshow("Trees", trees)

# borders
quote = cv2.copyMakeBorder(quote,20,20,20,20,cv2.BORDER_CONSTANT,value=(255,0,0))
cv2.imshow("Quote", quote)

cv2.waitKey(0)