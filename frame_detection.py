# using https://problemsolvingwithpython.com/11-Python-and-External-Hardware/11.04-Reading-a-Sensor-with-Python/

from puck_detector import puck_detector

import numpy as np
import cv2
import serial
import time
import imutils
from imutils.video import VideoStream

pd = puck_detector()
(H, W) = (None, None)

# start video stream
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# set up the serial line
# ser = serial.Serial('COM4', 9600) #needs to match arduino port
ser = serial.Serial('/dev/cu.usbmodem14201', 9600) #mac port

hit_detected = False
data = []

while hit_detected == False:
    print("reading....")
    b = ser.readline()
    string_n = b.decode()
    string = string_n.rstrip()
    if string == "Hit":
        # if hit, take frame and run detector
        frame = vs.read()
        frame = imutils.resize(frame, width=400)

        pd.detect(frame)
        hit_detected = True
