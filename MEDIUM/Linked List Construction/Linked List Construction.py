# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:  # When the linked list is empty
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:  # When the linked list is empty
            self.head = node
            self.tail = node
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # When linked list contains only one node then nothing to insert
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        if node.prev is None:
            # Then we are dealing with the head, we are inserting before the head
            self.head = nodeToInsert

        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        if node.next is None:
            # Then we are dealing with the tail, we are inserting after the tail
            self.tail = nodeToInsert

        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            # Then we are suppossed to set head
            self.setHead(nodeToInsert)
            return

        currentPosition = 1
        node = self.head
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            # If node is None then we are suppossed to set tail
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            # As we need to traverse rest of the linked list hence we are using temporary variable so that
            # the node.next is not set to None while removing the node.
            NodeToRemove = node
            node = node.next
            if NodeToRemove.value == value:
                self.remove(NodeToRemove)

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev

        # When the node is not head or tail
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        node.prev = None
        node.next = None

    def containsNodeWithValue(self, value):

        node = self.head
        while node is not None and node.value != value:
            node = node.next

        return node is not None  # When value matches it will return true
















