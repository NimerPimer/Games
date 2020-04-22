"""
This is a mandelbrot set simple visualizer -
A complex num 'a + bi' is represented by a tuple = (a, b)

REPETITIONS = number of iterations to determine if a point blows up to
              infinity or stays in a close region to the center.

LIM = if after REPETITIONS iterations, the iteration formula's output is smaller then LIM,
      the point is included in the set.

DIVISION_FACTOR = the "resolution" of the output graph. This is the step size when generating
                  points in a certain line.

RIGHT/LEFT_X , UP/BOTTOM_Y = the size of the checked area.

"""

import numpy as np
import matplotlib.pyplot as plt
from Complex_operations import *

REPETITIONS = 10
LIM = 2
DIVISION_FACTOR = 0.01

RIGHT_X = 1
LEFT_X = -2
UP_Y = 1
BOTTOM_Y = -1


def mandelbrot_iterations(num):
    start = (0, 0)
    for i in range(REPETITIONS):
        z = complex_power(start)
        start = complex_plus(z, num)

    if complex_num_size(start) < LIM:
        return True
    else:
        return False


def point_generator():
    real = np.linspace(LEFT_X, RIGHT_X, int((RIGHT_X-LEFT_X)/DIVISION_FACTOR))
    imaginary = np.linspace(UP_Y, BOTTOM_Y, int((UP_Y-BOTTOM_Y)/DIVISION_FACTOR))
    points = []

    for i in real:
        for j in imaginary:
            check = mandelbrot_iterations((i, j))
            if check:
                points.append((i, j))
    return points


def main():

    points = point_generator()
    x = []
    y = []

    for i in points:
        x.append(i[0])
        y.append(i[1])

    plt.plot(x, y, '.', color='black')
    plt.show()


if __name__ == "__main__":
    main()

