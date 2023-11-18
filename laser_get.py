# import the opencv library 
import cv2
import math
import numpy as np


def start_video_capture():
    # define a video capture object
    vid = cv2.VideoCapture(0)
    return vid


def display_stream_and_calculate_light(vid):
    while True:
        ret, frame = vid.read()
        # Display the resulting frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        else:
            pass
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (thresh, BandWimage) = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    conturs, _ = cv2.findContours(BandWimage, 1, 2)
    points = []
    for c in conturs:
        x, y, w, h = cv2.boundingRect(c)
        if w < 30 and h < 30:
            cv2.rectangle(BandWimage, (x, y), (x + w, y + h), 30, 3)
            points.append((x, y, gray[y, x]))
    cv2.imshow('frame', frame)
    return np.max(np.array(points), 2)


def stop_video(vid):
    vid.release()
    cv2.destroyAllWindows()
