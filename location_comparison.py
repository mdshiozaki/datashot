import math

def compare(x_shot, y_shot, x_target, y_target, cm_per_pixel):

    #ratio: 3:2
    x_diff = abs(x_target - x_shot)
    y_diff = abs(y_target - y_shot)

    diff_length_px = math.sqrt(x_diff**2 + y_diff**2)
    diff_length_cm = diff_length_px * cm_per_pixel

    return diff_length_cm
