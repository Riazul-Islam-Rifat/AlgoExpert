from collections import deque
def invertBinaryTree(tree):
    queue = deque()
    queue.append(tree)

    while len(queue):
        node = queue.popleft()
        if node is None:
            continue
        node.left,node.right = node.right,node.left
        queue.append(node.left)
        queue.append(node.right)

# Recursive solution
def invertBinaryTree(tree):
    if tree is None:
        return
    tree.left,tree.right = tree.right,tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
