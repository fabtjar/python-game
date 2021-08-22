import math


def approach(start, end, diff):
    if start < end:
        return min(start + diff, end)
    else:
        return max(start - diff, end)


def normalise(x, y):
    length = math.sqrt(x * x + y * y)
    return x / length, y / length


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
