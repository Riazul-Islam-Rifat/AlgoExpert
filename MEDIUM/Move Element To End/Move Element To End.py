def moveElementToEnd(array, toMove):
    leftPointer = 0
    rightPointer = len(array)-1

    while leftPointer < rightPointer:
        while array[rightPointer]==toMove and leftPointer < rightPointer:
            rightPointer-=1

        if array[leftPointer]==toMove:
            array[leftPointer],array[rightPointer]=array[rightPointer],array[leftPointer]
        leftPointer+=1
    return array