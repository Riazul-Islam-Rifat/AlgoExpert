# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # We will use siftDown method to build the heap from an array as it takes lower time than shiftUp
        # Find the first parent index [The one that is at the bottom of the tree]
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in range(firstParentIdx, -1, -1):
            # Find the consecutive next parent indexes and move it down if needed
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        # Find the child index of the parent (parent = currentIdx)
        childOneIdx = (currentIdx * 2) + 1
        # When the childOneIdx is a valid index
        while childOneIdx <= endIdx:
            # Find the child two index if it exists
            childTwoIdx = (currentIdx * 2) + 2 if currentIdx * 2 + 2 <= endIdx else -1
            # When childTwo exists and it's value smaller than childOne
            # We want to swap parent with childTwo as it is the minimum
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            # When child is smaller than parent then we want to move down the parent
            if heap[currentIdx] > heap[idxToSwap]:
                heap[currentIdx], heap[idxToSwap] = heap[idxToSwap], heap[currentIdx]
                # Now update the parent and child one index
                currentIdx = idxToSwap  # Parent moves to lower
                childOneIdx = (currentIdx * 2) + 1
            else:  # When the parent is lower, we simply end
                break

    def siftUp(self, currentIdx, heap):
        # Find out the parent index of the element that we want to shift up
        parentIdx = (currentIdx - 1) // 2
        # When we are not at the top of the tree and parent is greater than child, we want to move up
        while currentIdx > 0 and heap[parentIdx] > heap[currentIdx]:
            # Move up by swapping
            heap[parentIdx], heap[currentIdx] = heap[currentIdx], heap[parentIdx]
            # Update the currentIdx and parentIdx [For the while loop]
            # The previous parent index becomes the new current index
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        # Return the root of the heap
        return self.heap[0]

    def remove(self):
        # Here we are removing the first element of the heap
        # First we will swap the first element with the last elemet
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        removedVal = self.heap.pop()  # Remove the first element
        # Now the heap is not the same as previous
        # We have set the last element at the root:
        # now we will put it in the correct position using shiftDown
        self.siftDown(0, len(self.heap) - 1, self.heap)
        # Now return the removed value
        return removedVal

    def insert(self, value):
        # First we will insert he value at the end of the heap list
        # Then we will put it in the correct position using shiftUp method
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)  # The index we want to shift up
