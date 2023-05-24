# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    first = head.next
    second = head.next.next

    while first != second:
        first = first.next
        second = second.next.next

    # After the first while loop both first and second pointers are at the same point
    # From there the origin's distance is D and from head to origin is also D.
    # first = D + P
    # Second = 2D + 2P
    # Total = 2D + 2P - P --> Total = 2D + P
    # R = Total - D - P --> R = 2D + P - D - P
    #     --> R = D  [Head to loop origin == Same pointer to loop origin]
    # To get the origin do the following

    first = head

    while first != second:
        first = first.next
        second = second.next
    # Now both pointers point to the loop origin

    return first

