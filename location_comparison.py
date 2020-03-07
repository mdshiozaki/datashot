import math

def compare(x_shot, y_shot, x_target, y_target, px_to_cm):

    #ratio: 3:2
    x_diff = abs(x_target - x_shot)
    y_diff = abs(y_target - y_shot)xxxx

    diff_length_px = math.sqrt(x_diff**2 + y_diff**2)
    diff_length_cm = diff_length_px * px_to_cm

    return diff_length_cm
