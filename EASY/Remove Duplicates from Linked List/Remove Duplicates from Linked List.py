# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    # We never iterate the same element more than once
    currentNode = linkedList

    while currentNode:
        distinctNode = currentNode.next

        while distinctNode and currentNode.value==distinctNode.value:
            distinctNode = distinctNode.next

        currentNode.next = distinctNode
        currentNode = distinctNode


    return linkedList