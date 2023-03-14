# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):

    SumLinkedList = LinkedList(0) # Initiate a linked list
    currentNode = SumLinkedList # Pointer to the head node
    carry = 0 # Carry holds a number when sum > 9

    while linkedListOne or linkedListTwo or carry!=0:
        valOne = linkedListOne.value if linkedListOne is not None else 0
        valTwo= linkedListTwo.value if linkedListTwo is not None else 0

        sum = (valOne + valTwo + carry)%10
        carry = (valOne + valTwo + carry)//10

        # Add the sum in the SumLinkedList
        currentNode.next = LinkedList(sum)
        currentNode = currentNode.next
        linkedListOne = linkedListOne.next if linkedListOne is not None else None
        linkedListTwo = linkedListTwo.next if linkedListTwo is not None else None

    return SumLinkedList.next