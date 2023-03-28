# Most Optimal Solution

def minHeightBst(array):
    return CreateMinHeightBST(array, 0, len(array) - 1)


def CreateMinHeightBST(array, StartIndex, EndIndex):
    if EndIndex < StartIndex:
        return
    MidIndex = (StartIndex + EndIndex) // 2

    Bst = BST(array[MidIndex])
    Bst.left = CreateMinHeightBST(array, StartIndex, MidIndex - 1)
    Bst.right = CreateMinHeightBST(array, MidIndex + 1, EndIndex)

    return Bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
