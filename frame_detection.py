# using https://problemsolvingwithpython.com/11-Python-and-External-Hardware/11.04-Reading-a-Sensor-with-Python/

from puck_detector import puck_detector
from location_comparison import compare

import numpy as np
import cv2
import serial
import time
import imutils
from imutils.video import VideoStream

#

pd = puck_detector()
(H, W) = (None, None)

x_target = 250 # placeholder for taking in from csv file
y_target = 250 #placeholder for taking in from csv file

# start video stream
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# set up the serial line
# ser = serial.Serial('COM4', 9600) #needs to match arduino port
ser = serial.Serial('/dev/cu.usbmodem14201', 9600) #mac port

hit_detected = False
frame_queue = [] # queue of frames

while hit_detected == False:
    print("reading....")
    b = ser.readline()
    string_n = b.decode()
    string = string_n.rstrip()
    if string == "Hit":
        # if hit, take frame and run detector
        frame = vs.read()
        #add frame to queue
        frame_queue.append(frame)

        if len(frame_queue) == 10:
            # queue size max 10, ejects 10th oldest frame
            frame_queue.pop(0)

        x_shot, y_shot = pd.detect(frame_queue[0])
        diff = compare(x_shot, y_shot, x_target, y_target)
        print(diff)

        hit_detected = True
