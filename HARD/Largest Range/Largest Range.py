def largestRange(array):
    array.sort()
    tracker = [array[0], array[0]]
    start, end = array[0], array[0]
    for i in range(len(array) - 1):
        if array[i + 1] - array[i] > 1:
            end = array[i]
            if end - start >= tracker[1] - tracker[0]:  # >= To handle the cases like [-1,1,2...]
                tracker[0] = start
                tracker[1] = end
                start = array[i + 1]

        # To handle cases like [1,2,3,4,{6,7,8,9,10}]
        if i == len(array) - 2 and array[i + 1] - array[i] == 1:
            end = array[i + 1]
            if end - start > tracker[1] - tracker[0]:
                tracker[0] = start
                tracker[1] = end

    return tracker
