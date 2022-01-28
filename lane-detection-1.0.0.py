import cv2
vidcap = cv2.VideoCapture("ip.mp4")
success,image = vidcap.read()
count = 0
print("I am in success")
while success:
    success,image = vidcap.read()
    resize = cv2.resize(image, (640, 480)) 
    cv2.imshow("Result", resize)    
    if cv2.waitKey(10) == 27:                     
        break
    count += 1