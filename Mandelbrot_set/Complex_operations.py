"""
Some function for complex numbers calculations.

"""

import math
from operator import pow


def complex_num_size(num):
    return math.sqrt(pow(num[0], 2) + pow(num[1], 2))


def complex_power(num):
    new_a = pow(num[0], 2) - pow(num[1], 2)
    new_b = 2*num[0]*num[1]
    return new_a, new_b


def complex_plus(num_1, num_2):
    new_a = num_1[0] + num_2[0]
    new_b = num_1[1] + num_2[1]
    return new_a, new_b

