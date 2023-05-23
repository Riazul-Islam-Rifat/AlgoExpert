
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# p1-----> p2------>p3
def reverseLinkedList(head):
    current = head # p2
    prev = None # p1

    while current is not None:
        # We could initialize the next variable outside of the while loop but in that case we have a check an edge case of NULL value in each iteration
        next = current.next
        # current.next will indicate the previous node of the current node [As we are reversing]
        current.next = prev
        # In next iteration prev will be the running current node
        prev = current
        # In the next iteration current node will be the next node that we stored in next
        current = next
    # At the end of the while loop prev will be the head as it was the tail before
    return prev