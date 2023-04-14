# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Iterative solution
def symmetricalTree(tree):
    LeftStack = [tree.left]
    RightStack = [tree.right]

    while LeftStack:  # Check any one stack's length as both will be same
        leftNode = LeftStack.pop()
        rightNode = RightStack.pop()

        if leftNode is None and rightNode is None:
            continue
        # If one node is none and another is not node or values are not same
        if leftNode is None or rightNode is None or leftNode.value != rightNode.value:
            return False

        LeftStack.append(leftNode.left)
        LeftStack.append(leftNode.right)
        RightStack.append(rightNode.right)
        RightStack.append(rightNode.left)

    return True



