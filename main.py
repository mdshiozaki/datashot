# import dependencies
import numpy as np
import pandas as pd
from random import seed
from random import randint
import cv2
import serial
import time
import imutils
from imutils.video import VideoStream

# import from other files
from frame_detection import shot_detect
# from calibration import calibrate

# initiate
# set up the serial line
# ser = serial.Serial('COM4', 9600) # windows port
# ser = serial.Serial('/dev/cu.usbmodem14201', 9600) # mac port
# seed
seed(1)
results = []
# activate video
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start() # src=1 for usb camera
time.sleep(2.0)
print("[INFO] Ready")

# calibrate the camera for pixel to cm ratio
cm_per_pixel = calibrate(vs)

# get target coords
target_coords = pd.read_csv("shot_data.csv")
num_targets = sum(1 for line in target_coords)
print("Take your shot")

while (True):
	# if the `q` key was pressed, break from the loop
    frame = vs.read()
    cv2.imshow("frame", frame)
    cv2.waitKey(1)

    print("Shot")
    shot_result = shot_detect(vs, ser, num_targets, target_coords, cm_per_pixel)
    results.append(shot_result)
    print(shot_result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

    # if cv2.waitKey(1) & 0xFF == ord('w'):
    #     print("Shot")
    #     shot_result = shot_detect(vs, ser, num_targets, target_coords)
    #     results.append(shot_result)
    #     print(shot_result)

print(results)
cv2.destroyAllWindows()
