def bubbleSort(array):
    sorted = False
    counter = 0

    while not sorted:
        sorted = True
        for item in range(len(array) - 1):
            if array[item] > array[item + 1]:
                array[item], array[item + 1] = array[item + 1], array[item]
                sorted = False

        counter += 1 # Every time we omit the last element as it is the largest one. [So no comparison]

    return array
