import time

import cv2
import numpy as np


cap = cv2.VideoCapture(0)
frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
kernel = np.ones((5,5),np.uint8)

try:
    while True:
        success, img = cap.read()
        imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)
        imgCanny = cv2.Canny(imgBlur,30,30)
        imgDilated = cv2.dilate(imgCanny, kernel, iterations = 2)
        imgEroded = cv2.erode(imgDilated, kernel, iterations=2)
        
        cv2.imshow("Image", img)
        cv2.imshow("Gray", imgGray )
        cv2.imshow("Blurred", imgBlur )
        cv2.imshow("Canny", imgCanny )
        cv2.imshow("Dilated", imgDilated )
        cv2.imshow("Eroded", imgEroded )
        if cv2.waitKey(1) and 0xFF == ord('q'):
           break
except Exception as ex:
    print(ex)
finally:
    cap.release()
