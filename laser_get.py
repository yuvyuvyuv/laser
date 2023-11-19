# import the opencv library
import time

import cv2
import math
import numpy as np
import get_range


def start_video_capture():
    # define a video capture object
    vid = cv2.VideoCapture(0)
    return vid


def get_background(vid):
    t = time.time()
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    sum1 = np.zeros(gray.shape)
    i=0
    while time.time() < t+0.2:
        ret, frame = vid.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        sum1 += gray
        i += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            continue
        else:
            pass
    return int(sum1/i)


def display_stream_and_calculate_light(vid, frame_t_r):
    while True:
        ret, frame = vid.read()
        # Display the resulting frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            continue
        else:
            pass
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        (thresh, BandWimage) = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        conturs, _ = cv2.findContours(BandWimage, 1, 2)
        points = []
        color = []
        for c in conturs:
            x, y, w, h = cv2.boundingRect(c)
            if w < 30 and h < 30 and y < 380 and y > 180:
                points.append([x, y, w, h])
                color.append(gray[y, x])
        if color is []:
            print("Cant find")
        else:
            laser_point = points[np.argmax(color)]
            cv2.rectangle(BandWimage, (laser_point[0], laser_point[1]), (laser_point[0] + laser_point[2], laser_point[1] + laser_point[3]), 30, 3)
            print(laser_point)
        final_dist = get_range.get_range(320, laser_point[0])
        cv2.imshow('frame', BandWimage)

        print("distance to wall, from camera, is: ", final_dist)


def stop_video(vid):
    vid.release()
    cv2.destroyAllWindows()


def display_stream_and_calculate_light2(vid, frame_t_r):
    while True:
        ret, frame = vid.read()
        # Display the resulting frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            continue
        else:
            pass

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = gray - frame_t_r
        (thresh, BandWimage) = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        conturs, _ = cv2.findContours(BandWimage, 1, 2)
        points = []
        color = []
        for c in conturs:
            x, y, w, h = cv2.boundingRect(c)
            if w < 30 and h < 30 and y < 380 and y > 180:
                points.append([x, y, w, h])
                color.append(gray[y, x])
        if color is []:
            print("Cant find")
        else:
            laser_point = points[np.argmax(color)]
            cv2.rectangle(BandWimage, (laser_point[0], laser_point[1]),
                          (laser_point[0] + laser_point[2], laser_point[1] + laser_point[3]), 30, 3)
            print(laser_point)
        final_dist = get_range.get_range(320, laser_point[0])
        cv2.imshow('frame', BandWimage)

        print("distance to wall, from camera, is: ", final_dist)
