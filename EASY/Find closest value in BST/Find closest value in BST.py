def findClosestValueInBst(tree, target):
    closest = float('inf')
    current_node = tree

    while current_node is not None:

        if abs(current_node.value - target) < abs(target - closest):
            closest = current_node.value

        if current_node.value > target:
            current_node = current_node.left

        elif current_node.value < target:
            current_node = current_node.right

        else:
            break

    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
