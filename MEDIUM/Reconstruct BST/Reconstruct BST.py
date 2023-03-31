# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Defining a class to track the global varibale
class TreeInfo:
    def __init__(self, rootIndex):
        self.rootIndex = rootIndex


def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return constructBST(treeInfo, float('-inf'), float('inf'), preOrderTraversalValues)


def constructBST(currentNode, lower, upper, preOrderTraversalValues):
    if currentNode.rootIndex == len(preOrderTraversalValues):
        return None

    nodeValue = preOrderTraversalValues[currentNode.rootIndex]

    if nodeValue >= upper or nodeValue < lower:
        return None

    currentNode.rootIndex += 1
    leftNode = constructBST(currentNode, lower, nodeValue, preOrderTraversalValues)
    rightNode = constructBST(currentNode, nodeValue, upper, preOrderTraversalValues)

    return BST(nodeValue, leftNode, rightNode)


