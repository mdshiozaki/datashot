# using https://problemsolvingwithpython.com/11-Python-and-External-Hardware/11.04-Reading-a-Sensor-with-Python/

from puck_detector import detect
from location_comparison import compare

import numpy as np
import cv2
import time
import imutils
from imutils.video import VideoStream

def shot_detect(vs, ser, num_targets, target_coords, cm_per_pixel, x_zero, y_zero):
    (H, W) = (None, None)

    # obtain new target coordinates from csv
    index = randint(1, num_targets)
    x_target = target_coords['Net_X'][index]
    y_target = target_coords['Net_Y'][index]

    hit_detected = False
    # frame_queue = [] # queue of frames

    while hit_detected == False:
        print("reading....")
        b = ser.readline()
        string_n = b.decode()
        string = string_n.rstrip()
        if string == "Hit":
            # if hit, take frame and run detector
            time.sleep(0.1)
            frame = vs.read()
            #add frame to queue
            # frame_queue.append(frame)

            # if len(frame_queue) == 10:
            #     # queue size max 10, ejects 10th oldest frame
            #     frame_queue.pop(0)

            x_shot, y_shot = detect(frame)
            x_shot = x_shot - x_zero
            y_shot = y_shot - x_zero
            diff = compare(x_shot, y_shot, x_target, y_target, cm_per_pixel)

            hit_detected = True

    return diff
