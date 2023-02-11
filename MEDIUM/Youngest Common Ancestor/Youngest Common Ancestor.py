# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Find the depth of two descendants
    depthOne = findDepth(topAncestor, descendantOne)
    depthTwo = findDepth(topAncestor, descendantTwo)

    # Bring the farthest node at the same level of the other node
    if depthOne > depthTwo:
        return findYCL(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return findYCL(descendantTwo, descendantOne, depthTwo - depthOne)


def findDepth(topAncestor, descendant):
    depth = 0
    while descendant != topAncestor:
        descendant = descendant.ancestor
        depth += 1

    return depth


def findYCL(lowerDescendant, higherDescendant, diff):
    # This loop brings lowerDescendant at the same level
    while diff:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    # This loop finds the common ancestor
    while lowerDescendant.name != higherDescendant.name:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor

    return higherDescendant










