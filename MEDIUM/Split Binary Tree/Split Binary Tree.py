# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def splitBinaryTree(tree):
    desiredSum = totalSum(tree,0)/2
    splitPossible = splitTree(tree,desiredSum)[1]
    return desiredSum if splitPossible else 0

def splitTree(tree,desiredSum):
    if tree is None:
        return (0,False) # For leaf Node

    leftSum, LeftCanBeSplit = splitTree(tree.left,desiredSum) # First take left Value
    RightSum, RightCanBeSplit = splitTree(tree.right,desiredSum) # Then take right Value

    # Add left right and current value
    currentSum = leftSum + RightSum + tree.value
    canBeSplit = LeftCanBeSplit or RightCanBeSplit or currentSum == desiredSum
    # It will be true if currentSum is DesiredSum

    return (currentSum,canBeSplit)

def totalSum(tree, sum):
    if tree is None:
        return 0
    leftNode = totalSum(tree.left,sum) # Take left value
    rightNode = totalSum(tree.right,sum) # Take right value
    sum+= tree.value + leftNode + rightNode # Add left, right and current value
    return sum


