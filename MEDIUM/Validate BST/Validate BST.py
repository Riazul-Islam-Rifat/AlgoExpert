# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Initially set the maximum value to +Infinity
    # And set the minimum value to -Infinity
    # to check the root and then maximum and minimum value will be updated accordingly
    return ValidateBSTFinder(tree, float('-inf'), float('inf'))


def ValidateBSTFinder(tree, minimum, maximum):
    if tree is None:
        # Then we are at the leaf node so return True. Cause all the node above the leaf node satisfies the BST property
        return True

    if tree.value < minimum or tree.value >= maximum:
        return False  # As value must be smaller than minimum and greater than maximum

    # While traversing left side update the maximum value
    # While traversing right side update the minimum value
    LeftIsValid = ValidateBSTFinder(tree.left, minimum, tree.value)
    RightIsValid = ValidateBSTFinder(tree.right, tree.value, maximum)
    return LeftIsValid and RightIsValid

