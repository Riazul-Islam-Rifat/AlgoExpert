def quickSort(arr):
    sortHelper(arr, 0, len(arr) - 1)
    return arr


def sortHelper(arr, start, end):
    if start >= end:
        return
    pivotIdx = start
    left = pivotIdx + 1
    right = end  # To access the last index

    while left <= right:
        if arr[left] > arr[pivotIdx] and arr[right] < arr[pivotIdx]:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[left] <= arr[pivotIdx]:
            left += 1
        if arr[right] >= arr[pivotIdx]:
            right -= 1

    arr[pivotIdx], arr[right] = arr[right], arr[pivotIdx]
    leftArr = arr[pivotIdx + 1:right]
    rightArr = arr[right + 1::]
    sortHelper(arr, start, right - 1)
    sortHelper(arr, right + 1, end)

