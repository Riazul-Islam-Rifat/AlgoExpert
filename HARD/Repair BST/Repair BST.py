# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def repairBst(tree):
    # Find the swaped nodes and swap them again
    nodeOne = nodeTwo = prevNode = None

    def inOrder(node):

        nonlocal nodeOne, nodeTwo, prevNode
        if node is None:
            return

        inOrder(node.left)

        if prevNode is not None and prevNode.value > node.value:
            if nodeOne is None:
                nodeOne = prevNode
            nodeTwo = node
        prevNode = node

        inOrder(node.right)

    inOrder(tree)
    nodeOne.value, nodeTwo.value = nodeTwo.value, nodeOne.value
    return tree



