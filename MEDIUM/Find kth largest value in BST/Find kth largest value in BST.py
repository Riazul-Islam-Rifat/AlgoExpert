# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, numberOfVisitedNode, lastVisitedNodeValue):
        self.numberOfVisitedNode = numberOfVisitedNode
        self.lastVisitedNodeValue = lastVisitedNodeValue


def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0, 0)
    ReverseInOrderTraversal(tree, k, treeInfo)
    return treeInfo.lastVisitedNodeValue


def ReverseInOrderTraversal(node, k, treeInfo):
    if node is None or treeInfo.numberOfVisitedNode >= k:
        return

    ReverseInOrderTraversal(node.right, k, treeInfo)
    if treeInfo.numberOfVisitedNode < k:
        treeInfo.numberOfVisitedNode += 1
        treeInfo.lastVisitedNodeValue = node.value
        ReverseInOrderTraversal(node.left, k, treeInfo)
