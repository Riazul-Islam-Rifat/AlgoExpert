def firstDuplicateValue(array):
    for item in range(len(array)):
        absValue = abs(array[item])  # Take the absolute value of the current index
        index = absValue - 1  # Choose an index (absValue-1) to check whether the value of current index is repeated or not?
        if array[index] < 0:  # If the value(current index) is repeated then the choosen index's value will be negative
            return absValue  # Return the current index's absValue as the item is repeated
        array[index] = array[index] * -1  # Every time we make the choosen index's value nagtive
    return -1


