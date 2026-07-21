from typing import Tuple

import numpy as np

matrix_weight = 0.3
y_offset = -0.5

left_side = 0.2 # 0-220
middle    = - 0.1 # 220 - 420
right_side = 0.2  # 420 - 640

def motor_matrix(shape, left_side_gain, middle_gain, right_side_gain):

    res = np.zeros(shape=shape, dtype="float32")

    for x in range(0, 640):
        the_gain = middle_gain

        if x < 220:
            the_gain = left_side_gain
        elif x >= 420:
            the_gain = right_side_gain
        
        for y in range(0, 480):
            res[y, x] = the_gain

    return res

def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:

    res = motor_matrix(shape, -left_side, middle, right_side)
    
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    
    res = motor_matrix(shape, left_side, middle, -right_side)

    return res
