# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
    if tree is None:
        return treeInfo(0,0) # An object is returned here

    leftTree = getTreeInfo(tree.left)
    rightTree = getTreeInfo(tree.right)
    # After getting left and right sub tree as None for a particular root node or
    # After the complete traversal of left and right sub tree  for a particular root node
    PathThroughRoot = leftTree.height + rightTree.height
    diameter = max(PathThroughRoot, leftTree.diameter, rightTree.diameter)# Calculate diameter
    height = 1 + max(leftTree.height,rightTree.height) # Calculate height

    return treeInfo(diameter,height)

class treeInfo:
    def __init__(self,diameter,height):
        self.diameter = diameter
        self.height = height
