def selectionSort(array):
    # Every time we pick the smallest number and rearrange it's position in the sorted part of the given list
    currentIndex = 0  # First index of the unsorted list

    while currentIndex < len(array) - 1:
        smallestIndex = currentIndex
        for item in range(currentIndex + 1, len(array)):
            if array[item] < array[smallestIndex]:
                smallestIndex = item
        array[smallestIndex], array[currentIndex] = array[currentIndex], array[smallestIndex]
        currentIndex += 1

    return array

    # Index 0 to current index in the sorted part and the rest is the unsorted.

