def nodeDepths(root):
    # Write your code here.
    return depthSum(root,0)

def depthSum(root,depth):
    if root is None:
        return 0

    return depth + depthSum(root.left , depth+1) + depthSum(root.right, depth+1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
