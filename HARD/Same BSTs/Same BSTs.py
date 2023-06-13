def sameBsts(arrayOne, arrayTwo):
    # if the length of two given arrays are not same then we won't have same BST
    if len(arrayOne) != len(arrayTwo):
        return False

    # If we don't have any element in both arrays then we are in the base case
    # We are in the base case means all the other checks are okay, so we return True
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    # If the first element of both arrays don't match then the root is not same
    if arrayOne[0] != arrayTwo[0]:
        return False

    # When above everything is fine we look for the left&right subtrees of both arrays
    # if the subtress satisfies all the checks then both arrays can create same BST
    # Find arrays of the left and right subtrees recursively and check
    leftOne = getSmaller(arrayOne)  # Left subtree
    leftTwo = getSmaller(arrayTwo)  # Left subtree
    rightOne = getGreater(arrayOne)  # Right subtree
    rightTwo = getGreater(arrayTwo)  # Right subtree

    return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)


def getSmaller(arr):
    smaller = []
    for i in range(1, len(arr)):
        if arr[i] < arr[0]:
            smaller.append(arr[i])
    return smaller


def getGreater(arr):
    greater = []
    for i in range(1, len(arr)):
        if arr[i] >= arr[0]:
            greater.append(arr[i])
    return greater


