import cv2

trump = cv2.imread("trump.jpg")
trump_grayscale = cv2.cvtColor(trump,cv2.COLOR_BGR2GRAY)
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces = classifier.detectMultiScale(trump_grayscale,scaleFactor=1.5)
print(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(trump,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Face recognition",trump)

cv2.waitKey(0)