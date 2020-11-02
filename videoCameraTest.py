import time

import cv2
import numpy as np


cap = cv2.VideoCapture(0)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

try:
    while True:
        success, img = cap.read() 
        cv2.imshow("Result", img)
       
        if cv2.waitKey(1) and 0xFF == ord('q'):
           break
except Exception as ex:
    print(ex)
finally:
    cap.release()
