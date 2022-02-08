# Perspective Transformation!
import cv2
import numpy as np

vidcap = cv2.VideoCapture("ip.mp4")
success,image = vidcap.read()
count = 0
print("I am in success")
while success:
    success,image = vidcap.read()
    frame = cv2.resize(image, (640, 480)) 
    
    tl = (255,387)
    bl = (70 ,472)
    tr = (400,380)
    br = (538,472)
    
    # Perspective points to be warped
    cv2.circle(frame, tl, 5, (0,0,255), -1)
    cv2.circle(frame, bl, 5, (0,0,255), -1)
    cv2.circle(frame, tr, 5, (0,0,255), -1)
    cv2.circle(frame, br, 5, (0,0,255), -1)
    
    pts1 = np.float32([tl, bl, tr, br]) 
    pts2 = np.float32([[0, 0], [0, 480], [640, 0], [640, 480]]) 
    
    # Matrix to warp the image for birdseye window
    matrix = cv2.getPerspectiveTransform(pts1, pts2) 
    transformed_frame = cv2.warpPerspective(frame, matrix, (640,480))
    cv2.imshow("Bird's Eye View", transformed_frame)
    
    cv2.imshow("Result", frame)
    
    if cv2.waitKey(10) == 27:          # 'ESC' to quit program            
        break
    count += 1