def findThreeLargestNumbers(array):
    ThreeLargest = [None] * 3
    for item in array:
        UpdateThreelargest(ThreeLargest, item)
    return ThreeLargest


def UpdateThreelargest(ThreeLargest, item):
    if ThreeLargest[2] is None or ThreeLargest[2] < item:
        ShiftAndUpdate(ThreeLargest, 2, item)
    elif ThreeLargest[1] is None or ThreeLargest[1] < item:
        ShiftAndUpdate(ThreeLargest, 1, item)
    elif ThreeLargest[0] is None or ThreeLargest[0] < item:
        ShiftAndUpdate(ThreeLargest, 0, item)


def ShiftAndUpdate(ThreeLargest, index, number):
    for item in range(index + 1):
        if item == index:
            ThreeLargest[item] = number
        else:
            ThreeLargest[item] = ThreeLargest[item + 1]
