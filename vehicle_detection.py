import cv2

traffic = cv2.imread("traffic.png")
traffic_gs = cv2.cvtColor(traffic,cv2.COLOR_BGR2GRAY)
classifier = cv2.CascadeClassifier("cars.xml")

vehicles = classifier.detectMultiScale(traffic_gs,scaleFactor=1.5)
print(vehicles)

