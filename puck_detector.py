# based on https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
# requires opencv, numpy, python3,

import numpy as np
import cv2
import argparse

# Read image
#im = cv2.imread("puck_test.jpg")


# boundaries = [
#         #([10, 10, 100], [80, 130, 255]) # G B R
#         #([15, 0, 80], [55, 130, 255]) # RGB vals
#         ([3, 50, 50], [13, 255, 255]) #hsv?
#     ]
# for (lower, upper) in boundaries:
#     lower = np.array(lower, dtype = "uint8")
#     upper = np.array(upper, dtype = "uint8")
#
#     hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
#     mask = cv2.inRange(hsv, lower, upper)
#     output = cv2.bitwise_and(im, im, mask = mask)
#
# gray_im = cv2.cvtColor(output.astype("float32"), cv2.COLOR_BGR2GRAY)
# (X, Y) = gray_im.shape
# print(gray_im)
class puck_detector():

    def detect(self, img):
        im = img

        ORANGE_MIN = np.array([4, 50, 50],np.uint8)
        ORANGE_MAX = np.array([13, 255, 255],np.uint8)

        hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        frame_threshed = cv2.inRange(hsv_img, ORANGE_MIN, ORANGE_MAX)

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
            print(x_cen, y_cen)

            # draw the biggest contour (c) in green
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.circle(im, (x_cen, y_cen), 2, (0,255,0), 1)

        cv2.imshow("imgray", frame_threshed)
        cv2.imshow("im", im)

        #cv2.waitKey(0)

        return x_cen, y_cen
