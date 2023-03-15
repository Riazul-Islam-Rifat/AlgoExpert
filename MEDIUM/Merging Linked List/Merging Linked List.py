# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    currentNodeOne = linkedListOne
    currentNodeTwo = linkedListTwo

    while currentNodeOne is not currentNodeTwo:
        if currentNodeOne is None:
            currentNodeOne = linkedListTwo
        else:
            currentNodeOne = currentNodeOne.next

        if currentNodeTwo is None:
            currentNodeTwo = linkedListOne
        else:
            currentNodeTwo = currentNodeTwo.next

    return currentNodeOne