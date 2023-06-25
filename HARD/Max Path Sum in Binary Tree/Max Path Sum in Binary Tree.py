def maxPathSum(tree):
    Sum, maxSum = mps(tree)
    return maxSum


def mps(tree):
    if tree is None:
        return (0, float("-inf"))  # One is branch sum another one is triangle sum / MaxSum

    leftMaxSumAsBranch, leftMaxPathSum = mps(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = mps(tree.right)
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    maxSumAsBranch = max(maxChildSumAsBranch + tree.value, tree.value)
    MaxSumAsTriangle = max(leftMaxSumAsBranch + rightMaxSumAsBranch + tree.value, maxSumAsBranch)
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, MaxSumAsTriangle)

    return (maxSumAsBranch, maxPathSum)