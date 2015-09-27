# game_screen.py
# Hack TX 2015 - Eddie Dugan, Jeffrey Xiong, May Zhong, Xilin Liu

import cv2
import numpy
from matplotlib import pyplot as plt


def video_capture(video_file):
    cap = cv2.VideoCapture(video_file)

    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print(count)
        # cv2.imshow('frame', gray)
        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return count

video_capture('test.mp4')



