def hasSingleCycle(array):
    elementsVisited = 0
    currentIndex = 0

    while elementsVisited < len(array):
        if elementsVisited > 0 and currentIndex == 0:
            return False
        elementsVisited += 1

        jump = array[currentIndex]
        nextIndex = (jump + currentIndex) % len(array)
        if nextIndex >= 0:
            currentIndex = nextIndex

        else:
            currentIndex = nextIndex + len(array)

    return currentIndex == 0