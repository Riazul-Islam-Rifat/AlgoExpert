def isMonotonic(array):
    isNonIncresing = True
    isNonDecreasing = True

    for item in range(len(array)-1):
        if array[item+1] - array[item]>0:
            isNonDecreasing = False

        if array[item+1]-array[item]<0:
            isNonIncresing = False

    return isNonIncresing or isNonDecreasing