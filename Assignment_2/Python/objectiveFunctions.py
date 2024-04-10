def absolute(x):
    sum = 0
    for d in range(len(x)):
        sum = sum + abs(x[d])
    return sum