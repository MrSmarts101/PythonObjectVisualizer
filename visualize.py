import numpy as np
import cv2
from ultralytics import YOLO
import keyboard
import pycocotools
print("Keyboard module imported successfully!")
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    cv2.imshow('frame',frame)

    if(cv2.waitKey(1) == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()