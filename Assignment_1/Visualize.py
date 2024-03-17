import numpy as np
import sys
import matplotlib.pyplot as plt



appr = int(sys.argv[1])
itr_count = int(sys.argv[2])
min = float(sys.argv[3])
max = float(sys.argv[4])
evalFuntion = int(sys.argv[5])
inputFile = "./Data/particleCoordsData" + str(appr) + ".txt"

data = np.loadtxt(inputFile, delimiter = ",")
data = np.round(data, decimals = 4)


def absEval(x, y):
    return abs(x) + abs(y)

def ackley1(x, y):
    term1 = -20 * np.exp(-0.2 * np.sqrt((1/2) * (np.square(x) + np.square(y))))
    term2 = np.exp((1/2) * ((np.cos(2 * np.pi * x)) + (np.cos(2 * np.pi * y))))
    term3 = 20 + np.e
    return term1 - term2 + term3

def alpine1(x, y):
    x_term = np.absolute(x * np.sin(x) + 0.1 * x)
    y_term = np.absolute(y * np.sin(y) + 0.1 * y)
    return x_term + y_term

def alpine2(x, y):
    x_term = np.sqrt(x) * np.sin(x)
    y_term = np.sqrt(y) * np.sin(y)
    return x_term * y_term

def step_2(x, y):
    x_term = np.square(np.floor(x + 0.5))
    y_term = np.square(np.floor(y + 0.5))
    return x_term + y_term

def schwefel2_23(x, y):
    x_term = x**10
    y_term = y**10
    return x_term + y_term

def step_3(x, y):
    x_term = np.floor(np.square(x))
    y_term = np.floor(np.square(y))
    return x_term + y_term

def shubert4(x, y):
    x_term = 0
    y_term = 0

    for j in range(1, 6):
        x_term = j * np.cos((j + 1) * x + j)
        y_term = j * np.cos((j + 1) * y + j)

    return x_term + y_term

def discus(x, y):
    x_term = 10**6 * np.square(x)
    y_term = np.square(y)
    return x_term + y_term

def eggCrate(x, y):
    x_term = np.square(x) + 24 * np.square(np.sin(x))
    y_term = np.square(y) + 24 * np.square(np.sin(y))
    return x_term + y_term

def deb1(x, y):
    x_term = np.power(np.sin(5 * np.pi * x), 6)
    y_term = np.power(np.sin(5 * np.pi * y), 6)
    return (-1/2) * (x_term + y_term)

x = np.linspace(min, max, 1000)
y = np.linspace(min, max, 1000)
X, Y = np.meshgrid(x, y)

Z = np.zeros(shape = X.shape)

if (evalFuntion == 0):
    Z = absEval(X, Y)
elif (evalFuntion == 1):
    Z = ackley1(X, Y)
elif (evalFuntion == 2):
    Z = alpine1(X, Y)
elif (evalFuntion == 3):
    Z = alpine2(X, Y)
elif (evalFuntion == 4):
    Z = step_2(X, Y)
elif (evalFuntion == 5):
    Z = schwefel2_23(X, Y)
elif (evalFuntion == 6):
    Z = step_3(X, Y)
elif (evalFuntion == 7):
    Z = shubert4(X, Y)
elif (evalFuntion == 8):
    Z = discus(X, Y)
elif (evalFuntion == 9):
    Z = eggCrate(X, Y)
elif (evalFuntion == 10):
    Z = deb1(X, Y)

plt.contourf(X, Y, Z)
plt.colorbar()

x_data = data[:,2]
y_data = data[:,3]
itrs = data[:,0]

for itr in range(itr_count):
    plt.clf()
    plt.contourf(X, Y, Z, 10)
    plt.colorbar()
    plt.title(itr)
    plt.xlim(min, max)
    plt.ylim(min, max)
    plt.scatter(x_data[itrs == itr], y_data[itrs == itr])
    plt.pause(0.1)

sys.exit(plt.show())
