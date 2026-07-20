from typing import Tuple

import numpy as np
matrix_weight = 0.3

def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")

    x_max = shape[1]
    y_max = shape[0] # Y counts from 0 (top) to y_max (bottom)

    print(f"L type: {type(res[0,0])}")
    for x in range(0, x_max):
        x_frac = (float(x) / x_max)
        y_frac = (x_frac - 1.0) ** 2
        for y in range(0, y_max):
            res[y, x] = y_frac
    
    return res


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    
    x_max = shape[1]
    y_max = shape[0]

    for x in range(0, x_max):
        x_frac = float(x) / x_max
        y_frac = x_frac ** 2
        for y in range(0, y_max):
            res[y, x] = y_frac
    
    return res
