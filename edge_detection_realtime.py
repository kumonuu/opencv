import cv2, os

camera = cv2.VideoCapture(0)

while True:
    open_camera, frames = camera.read()

    edges = cv2.Canny(frames,100,200)
    cv2.imshow("Realtime Edge Detection",edges)

    if cv2.waitKey(1) == 32:
        break