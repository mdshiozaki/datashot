# based on https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
# requires opencv, numpy, python3

import numpy as np
import cv2
import argparse
import math
import imutils

def detect(img):
    im = img
    x_cen = 0
    y_cen = 0

    # ORANGE_MIN = np.array([4, 139, 130],np.uint8)
    # ORANGE_MAX = np.array([12, 255, 255],np.uint8)
    COLOUR_MIN = np.array([50, 100, 110],np.uint8) # green puck
    COLOUR_MAX = np.array([66, 255, 255],np.uint8) # green puck 

    hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    frame_threshed = cv2.inRange(hsv_img, COLOUR_MIN, COLOUR_MAX)

    contours,hierarchy = cv2.findContours(frame_threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0:
        # draw in blue the contours that were founded
        cv2.drawContours(im, contours, -1, 255, 3)

        # find the biggest countour (c) by the area
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)

        # centroid of largest contour
        x_cen = int((x+x+w)/2)
        y_cen = int((y+y+h)/2)
        print("Puck Center: ", x_cen, y_cen)

        # draw the biggest contour (c) in green
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.circle(im, (x_cen, y_cen), 2, (0,255,0), 1)

    # cv2.imshow("imgray", frame_threshed)
    cv2.imshow("im", im)

    return x_cen, y_cen
