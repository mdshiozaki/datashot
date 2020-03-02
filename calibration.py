import math
import imutils
from imutils.video import VideoStream



def calibrate():

    PINK_MIN = np.array([4, 50, 50],np.uint8) #change these for green
    PINK_MAX = np.array([13, 255, 255],np.uint8)

    hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    frame_threshed = cv2.inRange(hsv_img, PINK_MIN, PINK_MAX)

    contours,hierarchy = cv2.findContours(frame_threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


    dot_area_1 = 5
    dot_area_2 = 40
    xcnts = []
    for cnt in contours:
        if dot_area_1 < cv2.contourArea(cnt) < dot_area_2:




    x_dist =


return
