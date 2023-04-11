# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# We use TreeInfo class to track the variables we need
# Instead of returning x,y we return the object of TreeInfo class
class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height

def heightBalancedBinaryTree(tree):
    # Write your code here.
    return getBalancedTree(tree).isBalanced # Call the function where logic will be written

def getBalancedTree(node):
    # Base case
    if node is None:
        return TreeInfo(True,-1) # Leaf nodes are always balanced with no height, hence True,-1
    LeftBalancedTree = getBalancedTree(node.left)
    RightBalancedTree = getBalancedTree(node.right)
    isBalanced = LeftBalancedTree.isBalanced and RightBalancedTree.isBalanced and abs(
        LeftBalancedTree.height - RightBalancedTree.height)<=1
    height = max(LeftBalancedTree.height,RightBalancedTree.height)+1
    return TreeInfo(isBalanced,height) # return TRUE/FALSE and height