def mergeSort(arr):
    if len(arr) == 1:  # This is the base case. Single element is already sorted
        return arr
    # When there are multiple elements we start dividing and conquering
    midPoint = (0 + len(arr)) // 2
    leftArr = arr[0:midPoint]
    rightArr = arr[midPoint:len(arr)]

    mergeSort(leftArr)
    print('The left array is -- ', leftArr)
    mergeSort(rightArr)
    print('The right array is -- ', rightArr)
    i = j = k = 0
    print('Array before merging -- ', arr)

    # Merge two unsorted array
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] < rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
            k += 1
        elif leftArr[i] > rightArr[j]:
            arr[k] = rightArr[j]
            j += 1
            k += 1
        else:
            arr[k] = leftArr[i]
            k += 1
            i += 1
            arr[k] = rightArr[j]
            k += 1
            j += 1
    while i < len(leftArr):
        arr[k] = leftArr[i]
        i += 1
        k += 1
    while j < len(rightArr):
        arr[k] = rightArr[j]
        k += 1
        j += 1

    print('Array after merging -- ', arr)

    return arr
