import cv2 

cam = cv2.VideoCapture(0)
while True:
     
    frame = cam.read()
    cv2.imwrite(filename='capture.jpg', img=frame)
    cam.release()
    break