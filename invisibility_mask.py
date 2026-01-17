import cv2, numpy as np

camera = cv2.VideoCapture(0)

for i in range(60):
    open_camera, bg = camera.read()

bg = np.flip(bg,axis=1)

while True:
    open_camera, frames2 = camera.read()
    frames2 = np.flip(frames2,axis=1)
    frames = cv2.cvtColor(frames2,cv2.COLOR_BGR2HSV)

    lower_red = np.array([155,40,40])
    higher_red = np.array([180,255,255])
    mask1 = cv2.inRange(frames,lower_red,higher_red)
    mask2 = cv2.inRange(frames,np.array([100,40,40]),np.array([100,255,255]))
    combined_mask = mask1 + mask2

    # preprocessing
    combined_mask = cv2.morphologyEx(combined_mask,cv2.MORPH_OPEN,np.ones((3,3)),iterations=2)
    combined_mask = cv2.dilate(combined_mask,np.ones((3,3)),iterations=1)
    inverted_mask = cv2.bitwise_not(combined_mask)
    bg2 = cv2.bitwise_and(bg,bg,mask=combined_mask)
    frames3 = cv2.bitwise_and(frames2,frames2,mask=inverted_mask)
    weighted_sum = cv2.addWeighted(bg2,1.0,frames3,1.0,0)

    cv2.imshow("Invisibility Mask",weighted_sum)
    
    if cv2.waitKey(1) == 32:
        break 