import cv2, os

images = os.listdir("Images")
video_writer = cv2.VideoWriter("video.mp4",cv2.VideoWriter_fourcc(*'DIVX'),30,(1280,720))

print(os.path.splitext('Images/110.jpg'))

for i in range(len(images)-1,0,-1):
    frame = cv2.imread('Images/'+images[i])
    video_writer.write(frame)

video_writer.release()