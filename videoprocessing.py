import cv2

camera = cv2.VideoCapture(0)

while True:
    open_camera, frames = camera.read()
    cv2.imshow("Frames",frames)
    
    if cv2.waitKey(1) == 32:
        break