import math
import imutils
import cv2
import numpy as np
import time
from imutils.video import VideoStream


def calibrate(videostream):
    im = videostream.read()

    PINK_MIN = np.array([160, 70, 50],np.uint8)
    PINK_MAX = np.array([180, 255, 255],np.uint8)
    x_dist_cm = 146 # distance from TL to TR center circles
    y_dist_cm = 98  #find actual val

    hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    frame_threshed = cv2.inRange(hsv_img, PINK_MIN, PINK_MAX)

    contours,hierarchy = cv2.findContours(frame_threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        # draw in blue the contours that were founded
        cv2.drawContours(im, contours, -1, 255, 3)
        # sort contours according to contour area
        contours_sorted = sorted(contours, key=lambda x: cv2.contourArea(x))

        # top left circle
        top_left = contours_sorted[-1]
        xtl,ytl,wtl,htl = cv2.boundingRect(top_left)

        x_cen_tl = int((xtl+xtl+wtl)/2)
        y_cen_tl = int((ytl+ytl+htl)/2)
        # draw the biggest contour in green
        cv2.rectangle(im,(xtl,ytl),(xtl+wtl,ytl+htl),(0,255,0),2)
        # cv2.circle(im, (x_cen_tl, y_cen_tl), 2, (0,255,0), 1)

        # top right circle
        top_right = contours_sorted[-2]
        xtr,ytr,wtr,htr = cv2.boundingRect(top_right)

        x_cen_tr = int((xtr+xtr+wtr)/2)
        y_cen_tr = int((ytr+ytr+htr)/2)
        # draw the second biggest contour in red
        cv2.rectangle(im,(xtr,ytr),(xtr+wtr,ytr+htr),(0,0,255),2)
        # cv2.circle(im, (x_cen_tr, y_cen_tr), 2, (255,0,0), 1)


        #bottom right circle
        bottom_right = contours_sorted[-3]
        xbr,ybr,wbr,hbr = cv2.boundingRect(bottom_right)

        x_cen_br = int((xbr+xbr+wbr)/2)
        y_cen_br = int((ybr+ybr+hbr)/2)
        # draw the biggest contour (c) in green
        cv2.rectangle(im,(xbr,ybr),(xbr+wbr,ybr+hbr),(0,0,255),2)
        # cv2.circle(im, (x_cen_br, y_cen_br), 2, (255,0,0), 1)

        x_dist_px = x_cen_tr - x_cen_tl
        cm_per_pixel = x_dist_cm / x_dist_px

        y_dist_px = y_cen_tr - y_cen_br

        x_zero = x_cen_tl
        y_zero = y_cen_tl

        print(x_dist_px)
        print(cm_per_pixel)
        cv2.imshow('Contours', im)
        print("Press any key to continue")

        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()


    return cm_per_pixel, x_zero, y_zero
