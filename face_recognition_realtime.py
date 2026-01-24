import cv2

camera = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    open_camera, frames = camera.read()
    frames_grayscale = cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(frames_grayscale,scaleFactor=1.2)

    for (x,y,w,h) in faces:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow("Frames",frames)
    
    if cv2.waitKey(1) == 32:
        break