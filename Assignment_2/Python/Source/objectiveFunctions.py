import math
import numpy as np

def absolute(x):
    return np.sum(np.absolute(x))

def ackley_1(x):

    dimentions = float(len(x))
    term1 = -20.0 * np.exp(-0.2 * np.sqrt(np.sum(np.square(x)) / dimentions))
    term2 = np.exp(np.sum(np.cos(2.0 * np.pi * x)) / dimentions)

    return term1 - term2 + 20.0 + np.e

def alpine_1(x):
    return np.sum(np.absolute(x * np.sin(x) + 0.1 * x))

def step_2(x):
    return np.sum(np.square(np.floor(x + 0.5)))

def schwefel_2_23(x):
    return np.sum(np.power(x, 10))

def step_3(x):
    return np.sum(np.floor(np.square(x)))

def shubert_4(x):
    inner_sum = 0

    for j in range(5):
        inner_sum +=  float(j) * np.cos((j + 1) * x + j)

    dimentions = float(len(x))

    return np.sum(inner_sum) / dimentions

def discus(x):
    return np.power(10.0,6) * np.square(x[0]) + np.sum(np.square(np.delete(x, 0)))

def egg_crate(x):
    return np.sum(np.square(x)) + 24.0 * np.sum(np.square(np.sin(x)))

def deb1(x):
    dimentions = float(len(x))
    return -(np.sum(np.power(np.sin(5.0 * np.pi * x), 6)) / dimentions)
